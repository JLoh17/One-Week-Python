########## A LITTLE MORE ON STRINGS ##########
animal = 'catdog'

# Slice, the below picks the 2 and 3 but not including 4
print(animal[2:4])  # td

# If you put the last number big, it will only give you until the end
print(animal[2:99])  # tdog

# Leaving it blank means to the end, or if start from the beginning then to the end
print(animal[3:])  # dog

# The 3rd part (optional) shows a step
print(animal[::2])  # 3rd part shows a step, giving 'cto'

# Escape characters
# \n - Newline, space is not required
phrase = "new \nline"
print(phrase)
# \t - tab (gives a bit of space) "hello   world"
# \' - Single quote
# \" - Double quote
# \\ - Backslash

# Multiline strings can use triple quotes """ or ''' - used for addresses
print("""This
is
Triple Quotes
"!!!"
""")
