# Function are reuseable actions that have a name
# We use it to prevent code duplication
# Helps us abstract away code, break a complex program down into small pieces

# To write a function, we must 1) first define it, then 2) execute it
# Function syntax
def laugh():  # def = define, "laugh" is the name of a function (use snake_case)
    print("Ha " * 5)

# executing the function. The execution must happen after it is defined.
laugh()

# Function syntax with arguments
def lol(intensity):  # the parameter
    print("LOL " * intensity)

lol(1)  # the input is the argument
lol(3)

# Functions with multiple arguments
def divide(a, b):
    print(a/b)

divide(4,2)

# Introducing return - ends the execution of a function
# If we don't put return, the default value returned is None
def product(a,b):
    return(a*b)

variable = product(2,3)
print(variable) # 6

# Default parameters
# To give a parameter a default value if not argument is provided, simply add the default using this format: parameter = value
def laugh2(strength=2):
    print("Ha " * strength)

laugh2(5) # Ha Ha Ha Ha Ha
laugh2() # Ha Ha

# Ordering default parameters - put required parameters first, then default parameters after as Python doesn't know which parameters are being passed if you only pass one down below. You will get a syntax error afterwards
def greet(person, msg="Hi"): # required parameters before default parameter
    print(f'{msg}, {person}')

greet('Tonya')

# Keyword/named arguments - order doesn't matter
def get_total(price, qty=1, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal)

get_total(10,2,0.5)
get_total(qty=2, price=10, discount=0.5) # If I use keyword arguments, order doesn't matter, the results for both are still the same
