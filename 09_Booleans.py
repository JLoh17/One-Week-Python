########## BOOLEANS ##########
# Two possible values: True or False (note capitilisation - must be written as such)
isAlive = True

# Comparisons
# >, <, >=, <= all return a boolean
# == equal to (comparing to see if both the same), != not equal to
# 4.0 == 4 will show true (int and float is the same)

# False, 0.0, 0, None, empty strings/data structures = falsy, everything else is truthy!
bool(0)  # False
bool('Hello')  # True, even string '0' is truthy

# The 'in' operator
# Looks to see if an item is a member of a sequence (works for strings, not for int)
'a' in 'bat'  # True
'A' in 'abbA'  # True
4 in [4, 5, 99]  # True
43 in [4, 5, 99]  # False

# Python uses Unicode for encoding characters used in the string data type
# The function ord() will return the number for any character
ord('a')  # 97
ord('A')  # 65
