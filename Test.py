from modules.modul1 import MyClass1

#class main:


def main():
	a = MyClass1()
	print(a.myFunction1("Hello this is me in main function!"))

	a.run_thread()


print("*** main ***")
if __name__ == '__main__':main()


