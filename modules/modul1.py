import logging
import threading
import time
from modules.MyClass3 import MyClass3


class MyClass1(threading.Thread):

    def my_function1(self, message):
        print("** myFunction1 **")
        msg = "This is from MyClass1 message = " + message
        return msg

    def thread_function(self, name, name2):
        logging.info("Thread %s: starting  FROM: %s", name, name2)
        time.sleep(2)
        logging.info("Thread %s: finishing", name)

    def run_thread(self):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        logging.info("Main    : before creating thread")
        x = threading.Thread(target=self.thread_function, args=(1, "From Dario",))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        x.join()
        logging.info("Main    : all done")


