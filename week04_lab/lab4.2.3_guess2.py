# this program prompts the user to guess a number that the computer randomly generates
# the program will keep promting the user until they get it correct
# The program is adapted from the lab4.2.2_guess1.py program but this program will tell the user if they need to go higer or lower
# The program will also answer Q4 of the lab "get the prgram to generate a random number between 0 and 1000 to guess"
# Author: Stephen Kerr

# import random for the random number
import random

'''
# prompt the user for a number between the range
user_guess = int(input('Please guess a number between 1 and 10: '))
# generate the random number
computers_random_number = random.randint(1,10)
#print(computers_random_number)
# check if the user got the guess correct and prompt them to try again till it is correct
while user_guess != computers_random_number:
    # check if the user's guess is higher or lower than the random number
    if user_guess < computers_random_number:
        print(f' Sorry, {user_guess} is too low. Try again!!')
    else:
        # anything that is not equal to the random number or lower must be higher
        print(f'Sorry, {user_guess} is too high. Try again!!')
   # print(f'Sorry, that is not correct. Not thinking about {user_guess}.\nTry again!! ')
    user_guess = int(input('Please guess another number between 1 and 10: '))

print(f'How did you know I was thinking of {computers_random_number}.')
'''

# prompt the user for a number between the range
user_guess = int(input('Please guess a number between 1 and 100: '))


# generate the random number
computers_random_number = random.randint(1,100)
#print(computers_random_number)

# check if the user got the guess correct and prompt them to try again till it is correct
while user_guess != computers_random_number:
    # check if the user's guess is higher or lower than the random number
    if user_guess < computers_random_number:
        print(f' Sorry, {user_guess} is too low. Try again!!')
    else:
        # anything that is not equal to the random number or lower must be higher
        print(f'Sorry, {user_guess} is too high. Try again!!')
   # print(f'Sorry, that is not correct. Not thinking about {user_guess}.\nTry again!! ')
    user_guess = int(input('Please guess another number between 1 and 100: '))

print(f'How did you know I was thinking of {computers_random_number}.')
