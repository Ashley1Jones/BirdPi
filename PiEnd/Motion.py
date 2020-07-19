from Utils_Camera import *
from Motion import *
from Monitor import *
from FileSender import *
from multiprocessing import Event, Queue
from threading import Thread
import time
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--visual", type=str, default="n")
    args = parser.parse_args()
    # return
    finish = Event()
    qs = {"cam2motion": Queue(),
          "live_stream": Queue(),
          "change_cam": Queue(),
          "currently_rec": Queue()}
    evnts = {"motion": Event(),
             "recording": Event(),
             "finish": finish,
             "live_stream": Event()}

    # camera = Camera(qs, evnts)
    camera = ParrallelClass(target=Camera, finish=finish,
                            args=(qs, evnts, args.visual), Method=Thread, logName="Camera")
    motion_detector = ParrallelClass(MotionDetector, finish,
                                     (qs, evnts), Process, "Motion")
    file_sender = ParrallelClass(FileSender, finish,
                                 (qs, evnts, 9001), Process, "Sender")
    monitor = ParrallelClass(Monitor, finish, (evnts,), Thread, "Monitor")

    while not finish.is_set():
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            traceback_print_exc()
            # print("keyboard interrupt")
            finish.set()
    # join all threads and processes
    # file_sender.terminate()
    [pt.join(timeout=30) for pt in (camera, motion_detector, file_sender)]
    # [pt.terminate for pt in (file_sender,)]
    # emtpy queues and close
    for q in qs.values():
        # loop until empty
        while not q.empty():
            q.get(timeout=5)
        q.close()


if __name__ == "__main__":
    main()

