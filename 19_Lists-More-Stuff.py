# We can put booleans and None in lists
# We can also nest lists within lists

nums = [1,2,3,4,[5,6]] # the length shows 5
nums[4][1] # 6

# Concatenation - can only concatenate lists and lists
[1,2,3] + [4,5,6] # results in [1,2,3,4,5,6]

# Multiplication
[1,2,3] * 2 # [1,2,3,1,2,3]

# In operator
evens = [2,4,6]
4 in evens # True

# You can also do "not in"
# flavors = ['chocolate','vanilla','strawberry']

# response = input('What flavour would you like? ')

# while response.lower() not in flavors:
#     response = input('I don\'t know that flavor! Try again: ')

# print(f'OK, {response} ice-cream coming right up')

# Count - returns the number of times a values occurs in the list. If it does not exist, it returns 0
langs = ['Python','C','Javascript','C']
langs.count('C') # 2

# Reverse reverses a list in-place - changes the original
evens.reverse()
print(evens) # [6,4,2]

# Sort - sorts ascending, but can also sort by descending
evens.sort() # evens.sort(reverse = true)
print(evens) # [2,4,6]

# Each list is separately identified in memory (booleans, strings and numbers are always the same)

# Comparing lists
[1,2,3] == [1,2,3] # True, compares the contents and order of the list
[1,2,3] is [1,2,3] # False, compares the identity of the two lists (not the same as each list is identified differently in memory)

# Can use id() function to check the id of the variable

# split() is a string method that will split a string on a given character. It returns a list that holds the split strings
birthday = '03/27/2020'
birthday.split("/") # ['03','27','2020']

# join() is a string method that joins the elements of an iterable into a single string
fruits = ['Apple','Kiwi','Pear']
" ".join(fruits) # 'Apple Kiwi Pear'

# List unpacking (or destructuring) - we can unpack values form a list into specific variables. You cannot have less varibales on the right side than on the left
user = ['Joe','Bucky', 42]
first,last,age = user
print(f'''This is first: {first},
This is last: {last},
This is age: {age}''')

# * Unpacking - gathers remaining unassigned values into a variable
item = [4,'Pizza','Plain',16.98]
quantity, *others, price = item
print(f'''This is quantity: {quantity},
This is others: {others},
This is price: {price}''')

# copy() returns a shallow copy of a list (nested objects are not copied)
list1 = [12,9,3,7]
list2 = list1.copy() # Different ids but content still the same

# We can also copy with [:] - not the most readable
list3 = [12,9,3,7]
list2 = list1[:]
