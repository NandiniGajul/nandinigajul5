class father:
    def showf(self):
        print("Father class")

class son(father):
    def shows(self):
        print("From son class")


class daughter(father):
    def showd(self):
        print("From daughter class")


d=daughetr()
d.showd()
d.showf()