# this program prints out a random fruit
# Also answers Q6, Q7, Q8 in the week 3 lab
# Author: Stephen Kerr

# import the random module
import random

# fruits list
fruits = ['Apple', 'Orange', 'Banana', 'Pinapple', 'strawberry']

# generate a random number between 0 and the lenght of the fruits list - 1
index = random.randint(0, len(fruits)-1)

print(f'A Random Fruit: {fruits[index]}')

# Q6 Why does this code cause an error? How can we fix it? 
'''
message = 'I have eaten ' + 99 + ' burritos.'
print (message)
'''
# This code causes an error because you cannot concatenate a string with an integer.
# To fix this error, the integer 99 needs to be converted to a string.
# The code should be changed to:
message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

# Q7 Why is eggs a valid variable name while 100 is invalid? 
# Varriable names cannot start with a number, they can start with a letter or an underscore
# 100 is invalid because it starts with a number this will cause a SyntaxError
# eggs is valid because it starts with a letter

# What three functions can be used to get the integer, floating-point number, or string version of a value?
# int(), float(), str()