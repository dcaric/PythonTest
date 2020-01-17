import time
from modules.MyClass3 import MyClass3
from threading import Thread


class MyClass5(Thread):
    def __init__(self, thread_name, timer):
        super().__init__()
        self.thread_name = thread_name
        self.timer = timer

    def run(self):
        print(f'Class5 thread_name {self.thread_name} and timer {self.timer}')
        time.sleep(self.timer)
        print("Class5 end")
