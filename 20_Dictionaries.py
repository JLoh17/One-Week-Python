# Dictionaries (objects) allow us to store information as key-value pairs
# Keys can be any immutable type: numbers, strings, booleans or tupels (lists cannot be used) - note that the key must be unique
# Values can be whatever you want


# Creating dictionaries
empty_dict2 = {}
empty_dict1 = dict() # less common

# Syntax
movie = {'title':'Amadeus','imdb_score': 8.3}

# Accessing data in dictionaries - must match exactly (case matters!)
movie['title'] # Amadeus

# Adding and updating data in dictionaries
movie['title'] = 'AMADEUS' # changes the value
movie['imdb_score'] += 8.5 # updates to 16.8
movie['rating'] = 'R' # adds it to dict

# get() method and "in" operator

# In operator will only look at the key, not the values
order = {'cost': 3.5, 'quantity': 12}
12 in order # False
'cost' in order # True

# Get method will look for a given key in a dictionary. If the key exists, it will return the corresponding value, otherwise it returns None
order.get('chicken') # None
order.get('cost') # 3.5

# Pop, clear and del

# Pop accepts a key and will delete the corresponding key-value pair in the dictionary. It returns the deleted value
dict1 = {'a':1,'b':1,'c':3}
pop_value = dict1.pop('b') # 1

# Popitem deletes the most recently added key-value pair. It returns the item as a tuple.
dict2 = {'a':1,'b':1,'c':3}
pop_item = dict2.popitem() # ('c', 3)

# Clear deletes all items from a dictionary. It returns None
dict3 = {'a':1,'b':1,'c':3}
dict3.clear()
dict3 # {}

# del statement removes items from a dictionary. It is not a method.
dict4 = {'a':1,'b':1,'c':3}
del dict4['a']
dict4 # {'b':1, 'c':3}

# Dictionaries are mutable
# is and == works the same as lists (is) for reference memory and == for content

# Iterating Dicts: keys(), values() and items()
# Returns as a dict_items structure which is iterable (meaning we can use for/while loop)
order={'cost':3.5, 'quantity':12, 'product':'taco'}

# Keys
order.keys() # dict_keys(['cost','quantity',product'])

for item in order.keys(): # can exclude keys() - see below example
    print(item) # cost quantity product

for item in order: # no need to add .keys() as the default behaviour when iterating over dictionary is keys
    print(item) # this shows the same thing

# Values
order.values() # dict_values([3.5, 12, 'taco'])

# Items
order.items() # dict_items([('cost', 3.5), ('quantity', 12), ('product', 'taco')])

for k,v in order.items():
    print(k, v)

# We can convert any of these to a list:
list(order.keys()) # ['cost','quantity',product']

# Dictionary merging

# Update method will update the existing dictionary using key-value pairs from a secondary dictionary, passed as the argument
order = {'cost': 3.5, 'quantity': 12}
order_2 = {'cost': 4.5, 'date': '03/14/2019'} # cost will be updated to this one
order.update(order_2)
order # {'cost': 4.5, 'quantity': 12, 'date': '03/14/2019'}


# ** trick combines multiple dictionary into a new dictionary (dictionary unpacking)
dict1 = {'a':1, 'b': 2}
dict2 = {'c':1, 'd': 2}
dict3 = {**dict1, **dict2} # {'a':1, 'b': 2, 'c':1, 'd': 2}

# (Python 3.9 or later) dict union | will return a new dict containing items from left and right dicts. In the case of duplicated keys, the right side wins

dict1 = {'a':1, 'b': 2}
dict2 = {'c':1, 'd': 2}
dict3 = dict1 | dict2 # {'a':1, 'b': 2, 'c':1, 'd': 2}

# List and Dicts combined

# Nested dictionaries
music = {
    'gibson': {
        'location': 'USA',
        'price': 100,
    },
    'epiphone': {
        'location': 'China',
        'price': 50,
    }
}
music['epiphone']['location'] # China


# Dictionary of lists
test_scores = {
    'Marsha': [78,80,89],
    'Baker': [69,65,52]
}

# List of dictionaries
waitlist = [
    {
    'e-mail': 'tiff@gmail.com',
    'location': 'USA',
    'first_name': 'Tiffancy'
    },
    {
    'e-mail': 'tiff@gmail.com',
    'location': 'USA',
    'first_name': 'Tiffancy'
    }
]
