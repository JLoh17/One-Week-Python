# Working with Python modules
# A module is a python file that contains code that can be re-used in other files. It allows us to break up complex programs into smaller, more manageable pieces across multiple files

# 3 main types
# Built-in - Check the website for python standard library
# Custom
# 3rd party

# To use a module, we must import it first using the import keyword

import random
random.randint(1,6)

# Fancy import syntax
# Use the "as" keyword to import a module and give it a custom name in your script
import random as rand
rand.randint(1,6)

# Use the "from <module> import <method/class/constant>" syntax to import specific pieces of a module
from random import randint # from math import pi, sin if need multiple
randint(1,6)

# We can import all pieces of a module individually using import * however, this usually isn't the best approach to importing as it takes up space
# from random import *

# Creating custom modules - if it's in the same folder, can use "import" or "from <file> import <variable>"
import utils
print(utils.brand_colors)

from utils import brand_colors, mean
print(brand_colors)
print(mean([1,2,3,4,5]))

# 3rd party modules
# Pip is the python package installer that we can use to install hundreds of thousands of packages for use in our projects. It comes installed with Python3 now
# Go to PyPi.org
# "python3 -m pip install <package>" to install packages
# Best to check release date and number of downloads

import art
print(art.art('coffee'))
print(art.text2art('Hello'))
