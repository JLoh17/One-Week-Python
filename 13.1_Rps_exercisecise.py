from random import randint

rock = "rock"

paper = "paper"

scissors = 'scissors'
# Pick a random number from 1 to 3
num = randint(1, 3)

# Turn that random number into the computer's RPS move
if num == 1:
    comp_move = rock
elif num == 2:
    comp_move = paper
else:
    comp_move = scissors

# Ask a user to enter their move
user_move = input('Please enter your move (rock, paper or scissors): ').lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print(f'You played {user_move}')

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f'Computer played {comp_move}')

# Figure out who wins and print the result!
if user_move == comp_move:
    print("It's a tie")
elif user_move == 'scissors' and comp_move == 'paper' or user_move == 'rock' and comp_move == 'scissors' or user_move == 'paper' and comp_move == 'rock':
    print('You win!')
else:
    print('You lose')
