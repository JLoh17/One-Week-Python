# *args - use the wildcard or *notation to write functions that accept any number of arguments. The parameter can be whatever you want, but args is commonly used
# Gathers all remaining arguments in a tuple
# Take the function min or max, this uses *args

def count_stuff(*things):
    print(f"You passed me {len(things)} arguments")

count_stuff(1,2,3,4,5)

def silly(first,second,*others):
    print(f'first is: {first}')
    print(f'first is: {second}')
    print(f'first is: {others}')

silly(True,False,1,2,3,[])

# **kwargs (or keyword args) - we can use the ** notation to write functions that accept any number of keyword arguments (keyword where the parameter is color='red', age='12') and collects them as a dictionary which we can iterate over

def print_ages(**ages):
    print(f'this is what ** does {ages}')
    for k,v, in ages.items():
        print(f'{k} is {v} years old')

print_ages(max=67,sue=59)

# Parameter list ordering
# When defining functions, the order of parameter matters:
# (parameters, *args, default parameters, **kwargs)

def display_info(person,*args,status='singe',**kwargs):
    print(f'person is: {person}')
    print(f'args is: {args}') # this can be empty and just shows ()
    print(f'status is: {status}')
    print(f'status is: {kwargs}') # this can be empty and just shows {}

display_info('colt','purple',4,5,6,7) # first one print, the remaining arguments is printed as a tuple and status is not triggered
display_info('colt','purple',4,5,6,7,status='married') # by putting the keyword argument this will trigger the 3rd parameter
display_info('colt','purple',4,5,6,7,hello='married')

# A common gotcha with mutable objects as a parameter
def add_twice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    return lst

# Each list is its own list
add_twice(7,[1,2]) # [1,2,7,7]
add_twice(8,[1,2]) # [1,2,8,8]

# Will reuse the same list
add_twice(7) # [7,7]
add_twice(8) # [7,7,8,8]

# To fix this we do the following:
def add_twice(val, lst=None):
    if list is None:
      list = []
    lst.append(val)
    lst.append(val)
    return lst

# Unpacking args (spread operator so to speak)
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total/len(args)

nums = [1,2,3,4]
# average(nums) # this will not work as *args accepts them as individual arguments instead of a list
average(*nums) # What we can do is unpack the list using * in the argument
