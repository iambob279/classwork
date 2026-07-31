import random
class tressure:
    value = 0
    weight = 0
    name = ""

    def __init__(self, given_name):
        self.name = given_name
        self.weight = 20
        self.value = random.randint(1, 20)

    def new_name(self, newname):
        self.name = newname

    def showDetails(self):
        print(f"The value is {self.value}, the weight is {self.weight}, the name is {self.name}")

p = tressure("tressure name")
p.showDetails()