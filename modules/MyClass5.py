import time
from modules.MyClass3 import MyClass3
from threading import Thread


class MyClass5(Thread):

    def __init__(self, thread_name, timer):
        super().__init__()
        print("Constructor Class5")
        self.thread_name = thread_name
        self.timer = timer
        print(f'Class5 thread_name {self.thread_name} and timer {self.timer}')

    def run(self):
        print(f"Class5 begin time = {self.timer}")
        # b = MyClass3()
        time.sleep(self.timer)
        # b.func_from_class3("function3")
        print("Class5 end")

    def __del__(self):
        print("Destructor")
