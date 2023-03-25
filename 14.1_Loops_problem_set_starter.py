
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable

print(f'{"*"*10} Part 1a {"*"*10}')

for char in word:
    print(char)

# Write a while loop that does the same thing!
print(f'{"*"*10} Part 1b {"*"*10}')

idx = 0

while idx < len(word):
    print(word[idx])
    idx += 1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
print(f'{"*"*10} Part 2a {"*"*10}')

num = 100

while num < 141:
    print(num)
    num += 2

# Write a for loop that does the same thing (with range())
print(f'{"*"*10} Part 2b {"*"*10}')

for x in range(100, 141, 2):
    print(x)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
print(f'{"*"*10} Part 3 {"*"*10}')

reply = input('input the passphrase sillygoose: ').lower()

while reply != 'sillygoose':
    reply = input('Please input the passphrase sillygoose: ').lower()

print('Logged in!')
