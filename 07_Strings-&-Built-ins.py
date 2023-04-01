########## STRINGS & BUILT INS ##########
# Functions: func_name()
# Arguments: (fancy word for inputs) - burger(bun,secret_sauce). The arguments are bun and secret_sauce

# Length - len() will the return the length of a string; error for numbers
len('hello')  # length: 5, spaces don't count, ! counts

# help(len)  # help is another function that explains functions
# Press Q to quit

# Input prompts a user to enter some input, converts it to a STRING and then returns it
# To capture the input, you need to save it to a variable
first_name = input('what is your name? ')
print("Hi there " + first_name)

# Note, INPUT WILL ALWAYS BE SAVED AS A STRING

# Type accepts an input and returns the type of the object
# input() always gives a string
# Casting Types - converts types
int("12")  # converts string to integer
str(276)  # converts number to string
float(12)  # 12.0 - converts a string or number to float

# f-strings (formatting) - generates strings that contain interpolated expressions. Any code between {} will be evaluated and then the result will be turned into a string. Similar to template literals (didn't exist before python 3)
f"there are {24*60*60} seconds in a day"

age1 = 18
print(f"you are {age1} years old")
