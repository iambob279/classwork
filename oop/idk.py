class toyTank:
    colour = ""
    name = ""

    def __init__(self, given_colour, givenname):
        self.colour = given_colour
        self.name = givenname

    def getcolour(self):
        print(f"My colour is {self.colour}")

    def getName(self):
        print(f"My name is {self.name}")
    
    def setColour(self, newcolour):
        self.colour = newcolour
    
    def setName(self, newName):
        self.name = newName

tank = toyTank("blue", "A name")

tank.getcolour()
tank.getName()
