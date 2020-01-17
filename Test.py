from modules.modul1 import MyClass1
from modules.MyClass4 import MyClass4
from threading import Thread
import time


# class main:
def fun1():
    time.sleep(3)
    print("Working1")


def fun2():
    time.sleep(1)
    print("Working2")


def main():
    a = MyClass1()
    print(a.my_function1("Hello this is me in main function!"))
    # a.run_thread()

    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()

    b = MyClass4()
    t3 = Thread(name="worker1", target=b.worker1(10))
    t3.start()
    t4 = Thread(name="worker2", target=b.worker2(4))
    t4.start()


print("*** main ***")
if __name__ == '__main__': main()
