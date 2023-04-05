# Common error types
# SyntaxError - no colon
# NameError - wrong variable name
# IndexError - looking up an index that doesn't exist
# TypeError - adding strings with numbers
# ValueError - when a function receives an argument that has the right type but an inappropriate value (e.g. int('asd') - can take in a string but is not a number value)
# KeyError - looking up an invalid key in a dictionary

# Raising exceptions - we can raise our own exceptions (force them to happen) whenever we want, using the raise keyword
if not True:
    raise Exception('This is an error')
# Use the keyword Exception is generic, we can use any of the errors above

# When to raise
# Take the below function below. It asks for a username and saves it into a database
def get_user_name():
    user_input = input('please enter your name: ')
    if not user_input.isalpha():
        raise ValueError('alpha chars only')
    return user_input

def register_user():
    user = get_user_name()
    database.save(user)

register_user()

# try/except - we can use the keyword to handle exceptions. If an exception is raised in the try block, the except block with run
# try - code that could generate error
# except - code that runs if error raised
# except - usually better to except a specific exception rather than any possible exception

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Fine, I'll pick for you...7")
    num = 7
except EOFError:
    print("You didn't enter anything")
    num = 0
except (SyntaxError, NameError):
    print("oh no...")

print(f'You entered {num}')

# LBYL and EAFP

# LBYL - Look before you leap
# Coding style where you explicitly test for pre-conditions before making calls or "leaping". Characterized by lots of if statements

# EAFP - Easier to ask for forgiveness than permission "Assume things exists or will work, and catch exceptions if you're wrong"
# Coding style characterized by lots of try/except blocks
# The more Pythonic way of doing things
