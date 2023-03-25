# While loop - loop repeats as long as expression is true (i.e. stop running when condition evaluates to false)

answer = input('Please say hi ')


while answer != 'hi':
    # updates a variable until it satisfy the condition
    answer = input('Rude. Say hi...')

print("Thank you, hi to you too!")

###############
count = 1

while count <= 2:
    print(f'The count is: {count}')
    count += 1

# If you do an infinite loop, Ctrl + C for keyboard interrupt in the terminal to stop it

# For loop - iterates once per element
# Strings, [] (sets) are iterable

word = 'Hello'

for char in word:  # char is a variable up to us
    print(char)  # prints H E L L O on separate lines
# Note that you don't have to print the variable

# Range function in For loop
# If 1 argument: range(3) it starts from 0 and stops at the 1 argument. In this case it would be 0 1 2
# If 2 arguments: range(1,3), it starts from 1 and stops at 3. In this case it would be 1 2
# If 3 arguments: range(1,5,2), it starts from 1, jumps up by 2 each time and stops at 5 (does not print 5)

for num in range(1, 10, 2):  # start, stop (excluded), step
    print(num)  # 1 3 5 7 9
# Note that if you want to decrement, you cannot do (10, 0, 1) as the function will always increment by 1. Instead you have to do (10, 0, -1)

###############
for num in range(3):  # loops 3x
    print(num)  # 0 1 2
