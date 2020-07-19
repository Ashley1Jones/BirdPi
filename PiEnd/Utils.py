from threading import Thread, Event
from multiprocessing import Process, get_context
import traceback
import signal
import time
import sys
import threading
import ctypes
import logging
import os


def indent(text, num_indents=1):
    return f"{text:>{4 * num_indents}}"


def byteHeader(header, size):
    return bytes(f"{header:<{size}}", "utf-8")


def get_thread_id(t):
    # returns id of the respective thread
    if hasattr(t, '_thread_id'):
        return t._thread_id
    for id, thread in threading._active.items():
        if thread is t:
            return id


def kill_thread(t):
    thread_id = get_thread_id(t)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                     ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        print('Thread exception raise failure')


def create_log(name, lvl):
    log = logging.getLogger(name)
    log.setLevel(lvl)
    # formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    if lvl == logging.ERROR:
        lvl = "error"
    elif lvl == logging.INFO:
        lvl = "info"
    else:
        raise ValueError("incorrect logging level")
    file_handler = logging.FileHandler(f"log/{name}_{lvl}.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(message)s"))
    log.addHandler(file_handler)
    return log


def ParrallelClass(target, finish, args, Method, logName):
    """
    :param target: class to be targeted to be subprocess
    :param finish: finish event used to break loop
    :return: class object which overrides the process class
    """

    class Override(Method):
        def __init__(self, target, finish, args, logName):
            """
            overrides the Process class to create a seperate process containing this class only-
            input and output can be found in the subprocess and main process-
            """
            Method.__init__(self)
            self.finish = finish
            self.target = target
            self.args = args
            # create logging
            self.log_dir = f"log/{logName}.log"
            if not os.path.isdir("log"): os.mkdir("log")
            self.error_logger = create_log(name=target.__name__, lvl=logging.ERROR)
            # start thread or process with init
            self.start()

        def save_and_print_error(self, err):
            self.finish.set()
            traceback.print_exc()
            err = traceback.format_exc()
            self.error_logger.error(err)

        def run(self):
            """
            initialise used instead of init self because...
            memory from init self does not transfer to new class.

            Class requires three main methods;
                -init
                -main_loop
                -cleanup
            """
            try:
                if not (hasattr(target, "main_loop") and hasattr(target, "cleanup")):
                    raise AttributeError
            except Exception as e:
                self.save_and_print_error(e)
                return

            try:
                # init target class
                self.target = self.target(*self.args)
                while not self.finish.is_set():
                    self.target.main_loop()
            # if exception occurs, raise error and print
            except Exception as e:
                self.save_and_print_error(e)
            finally:
                # call class cleanup code
                try:
                    self.target.cleanup()
                except Exception as e:
                    self.save_and_print_error(e)

    return Override(target, finish, args, logName)

