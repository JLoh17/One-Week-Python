# Tuples - immutable, ordered collections
# Like lists but cannot be changed once created

dishes = ("burrito", "taco", "fajita") # separated by parenthesis
# tuple() is less common

# 1 item tuple
single_tuple = ("first") # not ok as parenthesis used for math
single_tuple = "first", # ok
single_tuple = ("first",) # ok

# Tuple functionality - index, len and slices work
# Index
dishes[0] # burrito

# Length
len(dishes) # 3

# Slice
dishes[1:3] # ('taco','fajita')

# Shows the index
dishes.index('burrito') # 0

# Counts how many times it is repeated
dishes.count('red') # 0

# In operator
"taco" in dishes # true

# For operator
for c in dishes:
    print(c)

# Why use tuples
# More efficient than lists
# Used for data that shouldn't change
# Can be used as keys in a dictionary

# Sets - unordered collections with no duplicate elements
# Only immutable elements can be in the sets
# We can add/delete elements, iterate over them and check to see if the element is in a list

evens = {2,4,6,8}

# To create an empty set:
set() # Must do this
set1 = {} # CANNOT DO THIS as this is a dictionary

# Working with sets
# add() - adds a single value to a set
even = {2,4,6,8}
even.add(12)
print(even) # {2,4,6,8,12}

# remove() - removes a single value from a set
even.remove(6)
print(even) # {2,4,8,12}

# discard() - like remove() but won't show error for missing value
even.remove(4)
print(even) # {2,8,12}

# clear() - empties out a sets
even.clear()
print(even) # set ()

# In operator looks
# For loop works

# Set operators: Intersection, Union, Difference
# Intersection - returns new set with members common to left and right
webdev = {'SQL','css','html','js','python'}
data = {'R', 'SQL', 'python'}
webdev & data #  {'SQL', 'python'}

# Union - returns new set with members from left and right
webdev_data = webdev | data
webdev_data # {'css', 'html', 'js', 'SQL', 'R', 'python'}

# Difference - returns new set with members from left not in right
diff = webdev - data
diff # {'CSS','html','js}

# When use sets
# Make it very easy/fast to check if a value exists in a collection
# Easy way to remove duplicates from a collection
