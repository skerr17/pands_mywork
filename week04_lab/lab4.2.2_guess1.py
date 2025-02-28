# this program prompts the user to guess a number that the computer randomly generates
# the program will keep promting the user until they get it correct
# Author: Stephen Kerr

# import random for the random number
import random

# prompt the user for a number between the range
user_guess = int(input('Please guess a number between 1 and 10: '))


# generate the random number
computers_random_number = random.randint(1,10)
#print(computers_random_number)

# check if the user got the guess correct and prompt them to try again till it is correct
while user_guess != computers_random_number:
    print(f'Sorry, that is not correct. Not thinking about {user_guess}.\nTry again!! ')
    user_guess = int(input('Please guess another number between 1 and 10: '))

print(f'How did you know I was thinking of {computers_random_number}.')
