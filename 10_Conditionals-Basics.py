from random import randint
import random
age = input('how old are you? ')
age = int(age)

# if condition:
#    "code that runs if condition if true" - typically 4 spaces of indentation

if age >= 21:
    print('Come on in!')
    print('*******')
print('AFTER THE IF STATEMENT')
# this gets printed regardless of True or False as not indented

# elif - Else If (if not the first thing, then try this instead)

# if test:
#     code if true
# elif test 2:
#     code if true

# Can have as many as you want
# elif only runs if nothing before it is true. So if you have 3 statements that are all true, it will print the first thing only then break
color = 'blue'

if color == 'green':
    print('BEGINNER!')
elif color == 'blue':
    print('INTERMEDIATE')
elif color == 'black':
    print('ADVANCED')

# Else - if none of the above were true, do this
# Must be after elif

# if age >= 21:
#     print('Come on in!')
# else:
#     print('Go home kid')

# the order is if, elif (as many as you want) and else

if age < 10:
    print('Your child ticket is $10')
elif age > 65:
    print('Your senior ticket is $12')
else:
    print('Your adult ticket is $14')

# asks for first name
# last name
# xxx is shorter than average american name
# 12 characters long

# Generating random numbers
# Comes with python, no need to download but need to import

# import random
random.randint(1, 6)  # generates a number between 1,6

# OR...

# from random import randint (this or above works)
randint(2, 10)
