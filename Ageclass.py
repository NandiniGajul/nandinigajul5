class Person:
    person="me"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getInfo(self):
        print("name is {self.name} and age is {self.age} ")

a=Person("a","10")
b=Person("b","25")
a.getInfo()
b.getInfo()