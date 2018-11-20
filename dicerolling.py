# Dice Rolling Simulator, created by Marek Woliński 2018-11-18
import random


def rolling():
    number = random.randint(1, sides)
    print('You rolled: %d' % number)


sides = input('How many sides you want to be your dice? ')
while not sides.isdigit():
    sides = input('You can\'t use this number, please try again: ')
else:
    sides = int(sides)

i = 1
while i == 1:
    rolling()
    again = input('Do you want to roll again (y/n)? ')
    while again != 'y' and again != 'n':
        again = input('Incorrect input, please try again: ')
    else:
        if again == 'y':
            i = 1
        else:
            end = input('Thanks for playing! \n(Press anything to leave.)')
            i = 0