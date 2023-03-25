########## THE WORLD OF METHODS ##########
# Methods are functions that "live" on objects
# thing.method() is the syntax like str.join()

# Capitilisation methods
msg = "Hello World"  # You dun need to put it in a variable
msg.capitalize()  # Hello world (makes first character uppercase and the rest lower)
msg.upper()  # HELLO WORLD
msg.lower()  # hell world
# Note that using a method does not change the original variable, unless we do for example msg = msg.capitalise()

# Documentation - Python.org (https://docs.python.org/3/)
# Library reference is the important one to click (language reference also good)

# Strip methods
# Strip removes whitespace (incl \n) from trailing and leading space only (not in between)
# str.strip([chars])  # [] means optional
",,.,.,.hello.,.,.,.,.".strip(".,")
# removes . or , at the beginning or end, not a combination
str.lstrip()  # removes to the left (i.e. leading)
str.rstrip()  # removes to the right (i.e. trailing)

# Replace methods
# str.replace(old, new, [count]): old and new is required, count is optional. If no count is given, it replaces all occurrences
prices = "$1.99  $9.25"
prices.replace('$', '')  # '1.99  9.25'

# Find and Index method
# str.find(sub[, start[,end]]) - Shows the lowest index of the substring u want. Start says start from which index (but doesn't required end), and end provides the range (but much have the start)
prices.find("$", 5)  # 7

# str.count(sub[, start[, end]]) - counts then number of time the string occurs

# Methods of Chaining
# Something.strip().lower() - the methods starts from left to right
# Cannot always chain methods if the method returns a number but generally it can
