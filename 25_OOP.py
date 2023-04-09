# Object Orientated Programming - an approach to programming that involves modeling "things" into Python objects. These objects can contain both data AND functionality all wrapped up together into a reusable component.

# Class are blueprints or recipes that we can late use to create objects from. A class describes what properties and functionality individual objects will contain.

# Instance - we call the individual objects that are created from a class blueprint, instances

# Creating a class
# class name is singular and capitalised (conventional, not mandatory)
class Dog:

    # Class attributes are kept for all instances
    species = 'canine'
    num_dogs = 0

    # special init method automatically called whenever new Dog is created. Self must be first parameter to init but it's always there. Name is defined by user.
    def __init__(self, name, breed, location):

        # self keyword refers to each individual object. In python this is usually called self but can be called anything (conventional)
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1

    # A method is a function in an object
    def bark(self):
        print(f'{self.name} says WOOF!')

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f'{self.name} performs {trick}')
        else:
            print(f'{self.name} does not know {trick} :(')

    # Class methods are available on the class directly, not associated with the specific instance of the class. Cls means Dog, that means if we change the class name we don't need to change it here
    @classmethod
    def register_stray(cls):
        return cls('coming soon', 'unknown', 'unknown')


# Every time we call Dog(), we're creating a new instance with its own name and tricks. Self is referring to the "Dog" instance
ott = Dog('Otter','Husky',94921)
ott.name # 'Husky'
ott.tricks # []
ott.bark()
ott.learn_trick('sit')
ott.learn_trick('stay')
print(ott.tricks)
ott.perform_trick('stay')

# You can manually change stuff without going into the class
ott.breed = 'pugmix'

# Class attribute
ott.species
ott.num_dogs

# Class method
stray1 = Dog.register_stray()
print(stray1.name, stray1.location, stray1.breed)

# Inheritance - where a class shares functionality from another class
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f'{self.name} meows!!')

# Every Cougar class inherits from class
class Cougar(Cat):
    def purr(self):
        print(f'{self.name} purrs!!')

class Lion(Cat):
    def __init__(self, name, pride_name):

        # super() calls Cat class as it shares the same name, so if we change Cat we don't need to change super
        super().__init__(name)
        self.pride_name = pride_name


    def roar(self):
        print(f'{self.name} roars!!')

c = Cat('blue')

puma = Cougar('tina')
puma.meow()
puma.purr() # c cannot do this

eli = Lion('eli')
eli.name()
eli.pride_name()
eli.roar() # puma cannot do this as inherits Cat class only

# The super() function - use this to refer to the base or parent class, instead of saying "Cat" class. We can also use this to access the __init__ method from the Cat class
