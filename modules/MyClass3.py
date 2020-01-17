from modules.MyClass2 import MyClass2


class MyClass3(MyClass2):
    b = "From Class3"

    def func_from_class3(self, info):
        print("This is function from Class3 calling " + info)
