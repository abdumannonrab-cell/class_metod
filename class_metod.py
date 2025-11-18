class Student:
    def __del__(self):
        print("del")
    def salom(self):
        print("salom1")

s1=Student()
s1.salom