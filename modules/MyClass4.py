import time
from modules.MyClass3 import MyClass3
import logging


class MyClass4:

    def __init__(self, thread_name, timer):
        super().__init__()
        self.thread_name = thread_name
        self.timer = timer

    def run(self):
        print(f"Thread {self.thread_name} timer {self.timer}")

    def worker(self):
        fomated = "%(asctime)s: %(message)s"
        logging.basicConfig(format=fomated, level=logging.INFO, datefmt="%H:%M:%S")
        logging.info("Thread %s: started", self.thread_name)
        b = MyClass3()
        time.sleep(self.timer)
        if self.thread_name == "Thread 1":
            b.func_from_class3("function3")
        else:
            b.func_from_class2("function2")
        logging.info("Thread %s: ended", self.thread_name)

