from modules.modul1 import MyClass1
from modules.MyClass4 import MyClass4
from modules.MyClass5 import MyClass5

import threading
import time
import multiprocessing


# class main:
def fun1():
    time.sleep(3)
    print("Working1")


def fun2(name):
    time.sleep(1)
    print(f"Working2 {name}")


def main():
    # a = MyClass1()
    # print(a.my_function1("Hello this is me in main function!"))
    # a.run_thread()

    # t1 = threading.Thread(target=fun1)
    # t2 = threading.Thread(target=fun2, args=('Mile',))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # print("First Thread")
    # t11 = MyClass5("Thread 1", 10)
    # t12 = MyClass5("Thread 2", 5)
    # t11.start()
    # t12.start()
    # t11.join()
    # t12.join()

    a = MyClass4("Thread 1", 10)
    b = MyClass4("Thread 2", 4)
    t3 = threading.Thread(name="worker1", target=a.worker)
    t4 = threading.Thread(name="worker2", target=b.worker)
    t3.start()
    t4.start()
    t3.join()
    t4.join()


print("*** main ***")
if __name__ == '__main__':
    main()
