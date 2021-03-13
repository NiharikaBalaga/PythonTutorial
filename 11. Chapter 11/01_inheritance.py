class Parent:
    Feature = "Tall"

    def showDetails(self):
        print("This is Father")

    def height(self):
        print("5'8")


class Child(Parent):
    language = "Tamil"
    # company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def height(self):
        print("6'0")
    # def showDetails(self):
    #     print("This is an programmer")


p = Parent()
p.showDetails()

r = Child()
r.getLanguage()
r.showDetails()
r.height()
