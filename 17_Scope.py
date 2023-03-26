# Scope
# Every variable we work with in python has a scope or boundary where it can be used used. There are specific rules to how variables are scoped based on where they are initially defined

# 4 main types of scoping
# Lexical, Enclosing, Global, Built-in (LEGB) - there is a reason for this order

# Global scope - variables declared outside of the function are in the global scope. All functions have access to them
movie = 'Amadeus'

def review():
    print(f'Outer: {movie}')
    def inner():
        print(f'Inner: {movie}')
    inner()

review()

# Local scope - variables defined in a function are scoped to that function. They are not available outside that function
def zoo():
    animal = "Shrimp"
    print('Inside zoo function: ', animal)

zoo()
# print('Outside zoo function: ', animal) <- this does not work

# Scope in loops and conditionals
# Variables in a loop/conditionals are not scored to that codeblock

for char in 'OCTOPUS':
    color = 'magenta'
    print(char)

print('AFTER LOOP:', color) # color can still be accessed

# Enclosing scope - nested 'inner' functions have access to variables declared in outer parent functions
def outer():
    animal = 'bird'
    print('OUTER FUNCTION:',animal) # this runs
    def inner():
        print('INSIDE INNER FUNCTION:',animal) # this also runs
    inner()

outer()

# Built-in scope - all built-in objects in Python are in the built-in scope. We have access to them anywhere!
num = 333
str(num)

# Scope precedence rules
# Python will check local scope first, then enclosing, then global, then built in

# The "Global" keyword - we can put this in front of variables to make them a global variable. Whether it is a good idea we will decide later but you may see it outside.

def outer():
    global animal
    animal = 'Crab'

outer()
print(animal)
