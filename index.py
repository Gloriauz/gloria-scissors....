import random

print('Make your choice:')
choice = input()
#choice = 'paper'
choice = choice.lower()
print("My choice is", choice)

choices = ['rock', 'paper', 'scissors']

computer_choice = choices[random.randint(0, len(choices)-1)]

print("computer_choice is", computer_choice)

if choice == 'rock':
    if computer_choice == 'rock':
        print('it is a tie')
    elif computer_choice == 'paper':
        print('Sorry, you failed :(')
    elif computer_choice == 'scissors':
        print('You win!!!! congrats :)')
if choice == 'paper':
    if computer_choice == 'paper':
        print('it is a tie')
    elif computer_choice == 'scissors':
        print('Sorry, you failed :(')
    elif computer_choice == 'rock':
        print('You win!!!! congrats :)')
if choice == 'scissors':
    if computer_choice == 'scissors':
        print('it is a tie')
    elif computer_choice == 'rock':
        print('Sorry, you failed :(')
    elif computer_choice == 'paper':
        print('You win!!!! congrats :)')
        print()