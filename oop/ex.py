class Person:
  #list attributes here
    first_name = ""
    last_name = ""
    address = ""
  
  #methods

    def __init__(self, given_first_name, given_last_name, living_address):
        self.first_name = given_first_name
        self.last_name = given_last_name
        self.address = living_address

    def show_full_name (self):
        print ("my name is", self.first_name, self.last_name)

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_first_name (self):
        return self.first_name
    
    def display_address(self):
        return self.address
        

p1 = Person("Rishi", "Sunak", "London")
p2 = Person("Keir", "Starmer", "Manchester")

p1.show_full_name()
p2.show_full_name()

print ("Name is currently", p1.get_first_name())
p1.set_first_name ("David")
print ("Name is now", p1.get_first_name())
p1.show_full_name()

print("p1 lives in", p1.display_address())