class father:
    def showf(self):
        print("Iam from parent class ")



class son(father):
    def shows(self):
        print("Iam from son")


class gson(son):
     def showsgs(self):
        print("Iam from gson")


s=gson()
s.shows()
s.showf()

s.showsgs()