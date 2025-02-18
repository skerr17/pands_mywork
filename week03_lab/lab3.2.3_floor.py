# this program takes in a float and outputs an int rounded down
# the math module is needed for this program 
# specifically the floor() function from the math module
# Author: Stephen Kerr

# import the math module
import math

# prompt the user for a float value
number = float(input("Enter a float number: "))

# round down the float number
number_rounded_down = math.floor(number)

# print the rounded down value
print(f'{number} rounded down is {number_rounded_down}')