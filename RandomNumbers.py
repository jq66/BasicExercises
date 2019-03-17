import random
import sys
import os

game = True
tries = 0
number = random.randint(1, 9)

while game == True:
    guess = int(input('What is your lucky number?: '))
    if guess < number:
        print('Oops! Looks like the number is bigger!')
        tries += 1
    elif guess > number:
        print('Oops! Looks like the number is smaller!')
        tries += 1
    elif guess == number:
        print('Congratulations! You guessed the number!')
        tries += 1
        if tries == 1:
            print('Awesome! You did it only in one try!')
            game = False
        elif tries > 1 and tries <= 3:
            print(f'Awesome! You did it only in {tries} tries!')
            game = False
        elif tries > 3 and tries < 10:
            print(f'Good! You did it in {tries} tries!')
            game = False
        else:
            print(f'That\'s bad! {tries} tries!')
            game = False

restart = input('Do you want to restart the game? (y/n): ')
if restart  == 'y':
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    print('Ok! Goodbye!')
