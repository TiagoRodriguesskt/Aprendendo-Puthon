from random import randint
from time import sleep

computer = randint(0, 10)

print('=' * 50)
print('\tLet s play guessing? ')
print('\tTry to hit the number I am thinking! ')
print('=' * 50)
player = int(input('Enter an integer from 0 to 10! '))
print('YOU...')
sleep(3)

if player == computer:
    print('CONGRATULATIONS! You are right!' )
else:
    print('LOST! I thought of the number {} and not the {}!'.format(computer, player))
