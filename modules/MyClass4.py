import time
from modules.MyClass3 import MyClass3


class MyClass4:

    def worker1(self, timer):
        print("worker1 begin")
        b = MyClass3()
        time.sleep(timer)
        b.func_from_class3("function3")
        print("worker1 end")

    def worker2(self, timer):
        print("worker2 begin")
        b = MyClass3()
        time.sleep(timer)
        b.func_from_class2("function2")
        print("worker2 end")
