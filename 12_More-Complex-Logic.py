# and, or, not

# logic 'and'
# Evaluates to True only if both left and right sides of the "and" evaluate to true, otherwise it's false
# 'a' == 'a' and 1 < 5 // True
# 'a' == 'a' true, 1 < 5 true

# A and B (if one side false then both false)

age = 19
print(age > 18 and age < 21)  # True

# logic 'or'
# Evaluate to true if one or both the left or right side evaluates to true
# 'a' == 'b' or 1 < 5 // True

True or False  # True
True or True  # True

day = input("what day of the week is it? ")

if day == 'saturday' or day == 'sunday':
    print("it's the weekend!")
else:
    print("ugh it's a workday :(")

# logic 'not'
# Changes true to false and false to true; it negates expression
# not and != are not the same thing
# 1 < 5 // true
# not 1 < 5 // false

temp = 19
not temp <= 0

# "432".isnumeric() returns true if string is a numeric string (i.e. "432"), false otherwise

year = input("what year were you born in? ")

if not year.isnumeric():
    year = input(
        "That isn't a number. Try again please! What year were you born in? ")  # would only repeat once if entered incorrectly
year = int(year)

print(f'You were born {2022-year} years ago')
