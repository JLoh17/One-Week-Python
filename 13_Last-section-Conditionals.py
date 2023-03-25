color = input('enter a color: ')

if color:  # instead of doing if color = '', this evaluates if truth or falsy. If color is an empty string, the following doesn't print
    print(f'{color} is my favourite color as well')

# Operator precedence: (), NOT, AND then OR

day = "Tuesday"
is_vet = False
age = 2

if age <= 2 or is_vet and day == "Tuesday":
    print("You get in for free today!")
