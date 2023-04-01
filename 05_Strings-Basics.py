########## STRING BASICS ##########
# You can use "" or '' for strings
color = "red"
print(color)

# Using "+" is concatenation without space
print("hello" + "world")  # helloworld

# Multiplication "*" works with a string and a number
print(3 * "ha")  # hahaha

# Strings are indexed starting with 0, -1 will be last one
msg = "I elov you"

msg[0]  # Shows "I", [1] shows space, anything outside is an error
# Note that this DOES NOT WORK with numbers

"asdf"[2]  # Shows "d"

# "None" defines lack of value, not 0 or an empty string (similar to null)
# "None" must be capital N
