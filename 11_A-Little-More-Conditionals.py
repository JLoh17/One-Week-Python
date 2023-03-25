# Python expects indentation after :
# Will show error if unusual indentation from the norm
# Cannot have elif or else on its own, only if

# Nesting conditionals
temp = 39
unit = 'celsius'

# Starts at the top first to check if true, otherwise won't run the inside
if unit == 'fahrenheit':
    if temp <= 32:
        print("It's freezing out!")
    else:
        print("It's not freezing")  # this runs
else:
    print("I'm really bad with celsius!")
