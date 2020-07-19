import socket
import numpy as np
import cv2
import time
import imutils
from multiprocessing import Process
import traceback


class MotionDetector(object):
    def __init__(self, qs, evnts):
        self.finish = evnts["finish"]
        self.input = qs["cam2motion"]
        self.motion_detected = evnts["motion"]
        # n moving pixels needed for detection
        self.sensitivity = 100
        # get first image
        self.last_gray = self.process_img(self.input.get(timeout=10))
        # set n seconds that motion is set after detection
        self.lag = 10
        #
        self.last_detected = time.time() - self.lag - 1

    def cleanup(self):
        pass

    def process_img(self, img):
        # convert image to grayscale and apply blur
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(gray, (21, 21), 0)

    def main_loop(self):
        # return back if no data available
        if not self.input.empty():
            img = self.input.get()
        else:
            time.sleep(1 / 50)
            return
        gray = self.process_img(img)
        # find difference between last frame and current frame
        frameDelta = cv2.absdiff(self.last_gray, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # finds where the difference is located within the image
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            #  if contour does not exceed a given area...
            # do not count is as motion detected
            if cv2.contourArea(c) < self.sensitivity:
                continue
            # old code to draw rectangles around movement
            # (x, y, w, h) = cv2.boundingRect(c)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.last_detected = time.time()

        self.last_gray = gray

        # if within lag time and not already set, set event
        if time.time() - self.last_detected < self.lag:
            if not self.motion_detected.is_set():
                self.motion_detected.set()
                print("--Motion detected--")
        else:
            if self.motion_detected.is_set():
                self.motion_detected.clear()
                print("--Switching off motion--")

