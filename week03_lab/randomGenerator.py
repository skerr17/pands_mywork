# this program prints out a random number between 1 and 10 
# author: Stephen Kerr

# import the random module
import random

'''
# prints out a random number between 1 and 10

number = random.randint(1,10)
print(f"Here is a random number {number} between 1 and 10")
'''


# Using user input for the number ranges

# prompt the user for the range start number
range_start = int(input("Enter the start of the range: "))

# prompt the user for the range end number
range_end = int(input("Enter the end of the range: "))


# generate the random number between the two user defined numbers
number_rand = random.randint(range_start, range_end)

# display the random number to the user 
print(f"Here is a random number {number_rand} between {range_start} and {range_end}")
