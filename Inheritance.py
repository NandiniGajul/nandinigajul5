class father:
    def __init__(self):
        self.fathername = "Dinesh"
        
    def show(self):
        print("constructor from father")


class son(father):
    def shows(self):
        print(" son class ")

s=son()
s.shows()
s.show()
print(s.fathername)