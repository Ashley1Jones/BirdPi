import socket
from Utils import *
import imagezmq
import cv2
from PyQt5 import QtGui, QtWidgets
import math


class Monitor(Thread):
    def __init__(self):
        self.file = "monitor.log"
        self.len = 10
        Thread.__init__(self)
        self.start_time = time.time()
        # create file if it doesnt exist
        with open(self.file, "w+") as _:
            pass
        self.start()

    def run(self):
        while time.time()-self.start_time < 15:
            with open(self.file, "r+") as file:
                f = file.readlines()
                if len(f) > self.len:
                    f = f[1:]
                f.append(f"{time.time()-self.start_time}\n")
                file.writelines(f)
                time.sleep(1)


class Communications(object):
    def __init__(self, signals):
        # this will be used to store all threads branching from this class
        self.thread_handler = ThreadPoolHandler()
        self.port = 9001
        self.headersize = 40
        self.add_to_terminal = signals[1]
        self.update_download_progress = signals[0]
        self.finish = Event()
        self.start_server()
        self.lock = Lock()
        self.live_stream_active = Event()
        self.live_stream_thread = None
        #self.thread_pool = []
        self.video_dir = "videos"
        if not os.path.isdir(self.video_dir): os.mkdir(self.video_dir)

    def start_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((socket.gethostname(), self.port))
        print(f"--Hosting server on name {socket.gethostname()} and port {self.port}--")
        self.s.listen(5)
        self.connected_cameras = {}
        self.accept_thread = self.thread_handler.add(Thread(target=self.connect_cameras, args=()))

    def change_cam_settings(self, exp, zoom, lr , bt):
        if len(self.connected_cameras) == 0:
            self.add_to_terminal.emit("No camera(s) connected")
            print("no cameras connected")
            return
        # change exposure to something the camera can read
        if exp == 50:
            exp = 0
        else:
            exp = int((exp/100)*(10000-500)+500)
        if zoom == 0:
            lr = 0
            bt = 0
        else:
            lr /= 100
            bt = (100 - bt) / 100
        zoom = (100-zoom)/100
        header = byteHeader(f"CHANGECAM-{exp}-{zoom}-{lr}-{bt}-", self.headersize)
        [com.send(header) for name, com in self.connected_cameras.items()]

    def get_files(self, buttons):
        self.button_list = buttons
        if len(self.connected_cameras) == 0:
            self.add_to_terminal.emit("No camera(s) connected")
            print("no cameras connected")
            #self.download_button.setDisabled(False)
            [b.setDisabled(False) for b in self.button_list]
            self.update_download_progress.emit(100)
            return
        self.thread_action(action=self._get_files)

    def play_pause_live_stream(self, pixmap=None):
        if not self.live_stream_active.is_set():
            if len(self.connected_cameras) == 0:
                self.add_to_terminal.emit("No camera(s) connected")
                return
            self.add_to_terminal.emit("Turning on live stream")
            self.live_stream_thread = self.thread_handler.add(Thread(target=self.live_stream, args=(pixmap,)))
            self.live_stream_active.set()
            #self.live_stream_thread.start()
        elif self.live_stream_active.is_set():
            self.add_to_terminal.emit("Turning off live stream")
            self.live_stream_active.clear()
            self.live_stream_thread.join(timeout=5)
            try:
                self.live_hub.close()
            except:
                traceback.print_exc()
            kill_thread(self.live_stream_thread)
            self.live_stream_thread = None

    def cleanup(self):
        # first tell cameras to close
        print("server closed and sending close command to cameras")
        [com.send(byteHeader("CLOSE-", self.headersize)) for name, com in self.connected_cameras.items()]
        [com.close() for name, com in self.connected_cameras.items()]
        print("sent end")
        self.finish.set()
        print("waiting for server to close")
        try:
            self.s.close()
        except:
            pass
        self.thread_handler.kill()

    def restart(self):
        self.cleanup()
        self.finish.clear()
        self.start_server()
        print("restarted server")
        self.add_to_terminal.emit("Successfully restarted server")

    def connect_cameras(self):
        """
        this functions launches the server socket
        each time client connects to the server, it is stored in a dictionary with the name sent from the client
        :param int - n_devices:
        :return: dict - client sockets, obj - main sockets
        """
        print("started server")
        while not self.finish.is_set():
            try:
                clientsocket, address = self.s.accept()
            except:
                time.sleep(1 / 10)
                continue
            print(f"--connection from address {address} has been established--")
            with self.lock:
                if address in self.connected_cameras:
                    self.add_to_terminal.emit(f"{address} tried to connect twice, closing prior connection")
                    self.connected_cameras[address].close()
                self.connected_cameras[address] = clientsocket
            self.add_to_terminal.emit(f"Connected new camera - {len(self.connected_cameras)} currently connected")
        self.s.close()

    def live_stream(self, pixmap):
        """
        uses imagezmq which handles all the hard stuff
        no need for threads, new connections are handled by imagezmq
        :return:
        """
        # send message to all clients to start stream
        [com.send(byteHeader("STREAMVIDEO-", self.headersize)) for _, com in self.connected_cameras.items()]
        self.live_hub = imagezmq.ImageHub()
        print("made live stream server")
        windows = {}
        width, height = pixmap.geometry().height(), pixmap.geometry().width()
        first = True
        while self.live_stream_active.is_set() and not self.finish.is_set():
            c_name, img = self.live_hub.recv_image()
            if first:
                if width < height:
                    new_width = width
                    new_height = math.floor((width/img.shape[1])*img.shape[0])
                else:
                    new_height = height
                    new_width = math.floor((height/img.shape[0])*img.shape[1])
                    first = False
            img = cv2.resize(img, (new_width, new_height))
            qim = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0],
                                   QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap.setPixmap(QtGui.QPixmap(qim))
            # verify that image was received
            self.live_hub.send_reply(b'OK')
        # tidy up
        pixmap.setText("Live Stream Closed")
        [com.send(byteHeader("STREAMVIDEO-", self.headersize)) for _, com in self.connected_cameras.items()]
        self.live_hub.close()
        cv2.destroyAllWindows()
        time.sleep(1)

    def thread_action(self, action):
        """
        :param action: function which is to be used on all connections
        :return:
        """
        cam_threads = {}
        for name, skt in self.connected_cameras.items():
            cam_threads[name] = self.thread_handler.add(Thread(target=action, args=(skt,)))

    def _get_files(self, skt, buffer=2 * 8 * 1024):
        """
        This function needs to be threaded.  Retrieves file size and name in header.
        Then loop to receive the whole file
        :param skt: individual client socket
        :param buffer: byte size of each buffer
        :return:
        """
        # send message with command
        skt.send(byteHeader("SENDFILES-", self.headersize))
        time.sleep(1)
        info = skt.recv(self.headersize).decode().split("-")
        n_files, downloading = int(info[0]), float(info[1])
        if n_files == 0:
            self.add_to_terminal.emit("No files to retrieve")
            # clear close from pipeline that otherwise be taken later
            skt.recv(self.headersize)
            #self.download_button.setDisabled(False)
            [b.setDisabled(False) for b in self.button_list]
            return
        downloaded = 0
        self.add_to_terminal.emit(f"Downloading {n_files} with size {int(downloading/10e6)}Mb")
        self.update_download_progress.emit(0)
        time.sleep(1)
        # first loop to collect all files
        while True:
            msg_string = b""
            msg = skt.recv(self.headersize)
            # if message is close, then close socket
            if msg[:5] == b"CLOSE":
                print("--end of messages--")
                break
            # gather message bytes length and name of file
            msg = msg.decode().split("-")
            msg_len, msg_name = int(msg[0]), msg[1]
            print(f"    new message size: {msg_len / (10e6)}Mb "
                  f"with name {msg_name}")
            # print(f"new message with name {msg}")
            # loop to read the rest of the buffers
            n_buffers = 0
            print_time = time.time()
            recv_msg_len = 0
            fname = f"{self.video_dir}/{msg_name}"
            with open(fname, "ab") as v:
                while True:
                    msg = skt.recv(buffer)
                    recv_msg_len += len(msg)
                    downloaded += len(msg)
                    v.write(msg)
                    # if length of message is matched then break
                    if recv_msg_len >= msg_len:
                        print(f"    {msg_name} received and sending feedback")
                        skt.send(bytes("video received", "utf-8"))
                        time.sleep(1)
                        break
                    n_buffers += 1
                    # only print every n seconds
                    if time.time() - print_time > 5:
                        print_time = time.time()
                        print(f"    first 5 bytes look like this {msg[:5]}")
                        print(f"    another {n_buffers} received, current message length {len(msg)}")
                        self.update_download_progress.emit(math.ceil(100 * downloaded / downloading))
                        n_buffers = 0
            self.update_download_progress.emit(math.ceil(100 * downloaded / downloading))
            #self.thread_handler.add(Thread(target=convert2mp4, args=(fname,)))
            print(f"    {msg_name} saved")
        print("finished downloading")
        self.update_download_progress.emit(int(100))
        #self.download_button.setDisabled(False)
        [b.setDisabled(False) for b in self.button_list]

