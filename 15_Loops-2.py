# break - we can use this keyword to prematurely exit a loop. Usually done inside of a conditional

import random from int
import random
for char in "apple":
    if char == 'l':
        break
    print(char)

print('After Loop')  # a p p afterloop

# continue - ends the current iteration of the loop, but does not break out

for char in "fatcat":
    if char in 'ac':
        continue
    print(char)

print('After Loop')  # f t t afterloop

# nested loops

for outer in range(1, 5):
    print(outer)
    for inner in range(1, 5):
        print("\t", inner)

###### DICE ROLLER EXERCISE #######
# from random import randint

# num_dice = int(input('How many dice are we rolling? '))
# num_sides = int(input('How many sides on each die? '))

# while True:
#     result = "|"
#     for die in range(num_dice):
#         rand = randint(1, num_sides)
#         result += f'{rand}|'
#     print(result)
#     reply = input("Roll again?' ('q' to quit) ")
#     if reply == 'q':
#         break

###### TOOTHPICK EXERCISE #######
# player1 = input("Enter player 1's name: ")
# player2 = input("Enter player 2's name: ")
# current_player = player1
# num_left = 13

# while True:
#     print('| ' * num_left)
#     print(f'There are {num_left} toothpicks left')

#     # Player choice
#     choice = int(input(f'How many do you take, {current_player}? '))
#     while choice != 1 and choice != 2 and choice != 3:
#         choice = int(input(f'You can only take 1, 2 or 3: '))
#     num_left -= choice

#     # Changes player turn
#     if num_left <= 0:
#         break
#     if current_player == player1:
#         current_player = player2
#     else:
#         current_player = player1

# print(f'{current_player} wins!!!')
# print('Game over!')
