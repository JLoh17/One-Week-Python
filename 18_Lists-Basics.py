# Data structure is a container that can contain multiple values at once
# Lists are ordered collections of data

# 1st way of creating lists - common method
high_scores = [99,78,56,50,20,12] # Syntax

# 2nd way of creating lists - less common
list('hello') # creates a list ['h','e','l','l','o']
list(range(3,7)) # [3,4,5,6]

# Accessing data in lists - index starts at 0
high_scores[0] # 99
high_scores[-1] # 12

len(high_scores) # 6 (different to index)

# Updating list elements
num_list = [7,3,9]
num_list[1] = 8 #[7,8,9]

# Append - adds a single value to the end of a list
nums = [1,2,3,4]
nums.append(5) # [1,2,3,4,5]

# Extend - accepts an iterable and appends each item to the end of the list
nums_2 = [1,2,3]
nums_2.extend('abc') # [1,2,3,'a','b','c']

# Insert - accepts 2 arguments. Index where to insert the element, and the element to be inserted into the list
num_list.insert(1,'hi') # [7,'hi',3,9]

# Slice - (start,stop,step)
# Start can be empty, or stop can be empty
# Note that the original list remains unchanged
stuff = ['c',6,'a',9,'t',6]
stuff[:2] # ['c','6']

stuff[0:5:2] # ['c','a','t']

# Using slice to add on to list (replaces original list)
nums[1:3] = ['a','b','c'] # [1, 'a', 'b', 'c', 4, 5]
nums[1:4] = [10] # [1,10,4,5]

# Clear removes all items for the list, but keeps the container
nums.clear()
print(nums)

# Remove - removes only the first element in the list that matches the argument
nums = [1,2,3,2,5]
nums.remove(2) # [1,3,2,5]

# Pop - removes the last element from the list and returns it
nums.pop() # 5, list becomes [1,3,2]
nums.pop(0) # 1, list becomes [3,2]

# Del - it is a statement (not a method) that can be used to delete an item from a specific index in a list
langs = ['python','c','javascript','c']
del langs[2] # does not return anything
langs # ['python','c','c']

# Iterating over lists
# Can use for/while loop
langs2 = ['python','c','javascript','c']

for lang in langs2:
    print(lang) # python, c, javascript, c
