# The Mammal 
class Mammal: #class represents a generic mammal.
    # attributes
    species = "Mammal" #default value
    # The __init__ method accepts an argument for
    # the mammal's species. 
    def __init__(self, given_species):
        self.species = given_species

    # The show_species method displays a message
    # indicating the mammal's species.
    def show_species(self):
        print('I am a', self.species)

    # The make_sound method is the mammal's
    # way of making a generic sound.

    def make_sound(self):
        print('Grrrrr')

# The Dog class is a subclass of the Mammal class.
class Dog(Mammal):
    # The __init__ method calls the superclass's
    # __init__ method passing 'Dog' as the species.
    def __init__(self):
        super().__init__('Dog')
    # The make_sound method overrides the superclass's
    # make_sound method.
    def make_sound(self):
        print('Woof! Woof!')


# The Cat class is a subclass of the Mammal class. 
class Cat(Mammal): 
    # The __init__ method calls the superclass's
    # __init__ method passing 'Cat' as the species. 
    def __init__(self):
        super().__init__('Cat') 
    # The make_sound method overrides the superclass's
    # make_sound method. 
    def make_sound(self):
        print('Meow')

class mouse(Mammal):
    def __init__(self):
        super().__init__("mouse")
    
    def make_sound(self):
        print("Squeak")


def main(): #demonstrates polymorphism.
# Create a a Mammal object, a Dog object, and a Cat object.
    choice = 0
    while choice!=4:
        new_animal= None
        choice = int(input ("Enter 1 for a dog, 2 for a cat, 3 for a mammal, 4 to exit: "))
        if choice == 1:
            new_animal = Dog()
        elif choice == 2:
            new_animal = Cat()
        elif choice == 3:
            new_animal = Mammal('regular animal')
        if new_animal is None:
            print ("New animal not chosen")
        else:
            new_animal.show_species()
            new_animal.make_sound()
    
 

    
# Call the main function.
main()