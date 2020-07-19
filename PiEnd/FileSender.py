import os
import time
import socket
import pickle
from multiprocessing import Process, Queue
from threading import Thread, Event
import threading
import imagezmq
import numpy as np
import traceback
from Utils import *
import random
import traceback


# import ctypes


class FileSender(object):
    def __init__(self, qs, evnts, port):
        self.path = "videos"
        self.HEADERSIZE = 40
        self.buffer = 8 * 1024
        self.finish = evnts["finish"]
        self.recording = evnts["recording"]
        self.live_event = evnts["live_stream"]
        self.live_queue = qs["live_stream"]
        self.cam_queue = qs["change_cam"]
        self.currently_rec = qs["currently_rec"]
        self.connected = False
        self.cam_name = "ADAM"
        self.server_names = ["DESKTOP-547KG8M", "Francis-PC"]
        self.port = port
        self.command_socket = None
        self.files_socket = None
        self.client_queue = Queue()
        self.command_thread = None
        time.sleep(2)

    def cleanup(self):
        # if command socket is still open close
        if self.command_socket:
            self.command_socket.close()
        # empty and close all remaining queues
        while not self.client_queue.empty():
            self.client_queue.get()
        self.client_queue.close()

    def connect_to_server(self):
        while not self.finish.is_set():
            for server in self.server_names:
                print(f"--Attempting connection with {server} on port {self.port}--")
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.settimeout(10)
                try:
                    self.s.connect((server, self.port))
                    print("--Connected to server--")
                    self.server_name = server
                    return
                    # break
                except:
                    print("    failed connecting")
                    # give time for closing
                    time.sleep(1)
                    # print("failed coms")
                    self.s.close()
                    self.s = None

    def main_loop(self):
        while not self.finish.is_set():
            # create thread to accept clients, while checking finish
            # try connection
            self.connect_to_server()
            # wait for socket to warm up
            time.sleep(1)
            if self.finish.is_set():
                break
            self.s.settimeout(None)
            self.get_execute_commands()

    def get_execute_commands(self):
        self.command_thread = None
        # count number of times 0 bytes have been sent
        zero_count = 0
        while not self.finish.is_set():
            # start thread that waits for 
            if self.command_thread is None:
                self.command_thread = Thread(target=self.receive_thread)
                self.command_thread.start()

            # if command queue not emtpy, collect data and close the thread
            if not self.client_queue.empty():
                command = self.client_queue.get()
                try:
                    message = command.decode().split("-")
                    command = message[0]
                except:
                    traceback.print_exc()
                # check for empty messages
                if len(command) == 0:
                    zero_count += 1
                    time.sleep(1 / 10)
                    continue
                # if they have exceeded n times, break
                if zero_count > 50:
                    self.s.close()
                    break
                self.command_thread.join()
                self.command_thread = None
            else:
                time.sleep(1 / 10)
                continue

            print(f"got command {command}")
            if command == "CHANGECAM":
                self.cam_queue.put(message[1:-1])
            if command == "SENDFILES":
                try:
                    self.send_files()
                except:
                    traceback.print_exc()
                    break
            if command == "STREAMVIDEO":
                if not self.live_event.is_set():
                    self.live_event.set()
                    print("starting livestream")
                    self.stream_thread = Thread(target=self.stream_video)
                    self.stream_thread.start()
                    continue
                if self.live_event.is_set():
                    self.live_event.clear()
                    print("ending livestream")
                    self.stream_thread.join()
                    continue
            if "CLOSE" in command:
                print("--got close command--")
                self.s.close()
                self.s = None
                break
        # when loop is broken, check for command thread and kill it!!!
        if self.command_thread is not None:
            kill_thread(self.command_thread)
        self.live_event.clear()

    def receive_thread(self):
        try:
            command = self.s.recv(self.HEADERSIZE)
            self.client_queue.put(command)
        except:
            self.client_queue.put("CLOSE")

    def stream_video(self):
        stream = imagezmq.ImageSender(connect_to=f'tcp://{self.server_name}:5555')
        try:
            while self.live_event.is_set() and not self.finish.is_set():
                if not self.live_queue.empty():
                    stream.send_image(self.cam_name,
                                      self.live_queue.get())
                time.sleep(1 / 10)
        except:
            traceback.print_exc()
            pass
        stream.close()
        print("closed stream on client end")

    def send_files(self):
        videos = os.listdir(self.path)
        total_size = 0
        for video in videos:
            total_size += os.path.getsize(f"{self.path}/{video}")
        if len(videos) == 0:
            print(indent("no files to send", 1))
        time.sleep(1)
        info = f"{len(videos)}-{total_size}-"
        self.s.send(bytes(f"{info:<{self.HEADERSIZE}}", "utf-8"))
        time.sleep(1)

        if not self.currently_rec.empty():
            openfile = self.currently_rec.get()
            print(f"{openfile} currently open")
        else:
            openfile = "dummy"

        for i, video in enumerate(videos):
            video_path = f"{self.path}/{video}"
            if video_path == openfile:
                print("still recording that one")
                continue
            with open(video_path, "rb") as v:
                l = os.path.getsize(video_path)
                if l < 1:
                    print("complete dud")
                    os.remove(video_path)
                    continue
                header = f"{l}-{video}"
                header = bytes(f"{header:<{self.HEADERSIZE}}", "utf-8")
                # header = bytes(f"{video:<{self.HEADERSIZE}}", "utf-8")
                print(f"    sending message with header: {header}")
                self.s.send(header)
                time.sleep(1)
                self.s.sendfile(v, 0)
            print(f"    sent {video} down the pipe")
            time.sleep(1)
            answer = self.s.recv(64)
            print(f"    got message back: {answer}")
            os.remove(video_path)
            print(f"    completed sending")
            time.sleep(1)

        print("--all files sent--\n")
        self.s.send(b"CLOSE")
        time.sleep(1)


