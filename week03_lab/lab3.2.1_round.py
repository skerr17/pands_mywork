# this program should take in a float and output an integer (round up or down)
# Author: Stephen Kerr

# prompt the user for a float number
number_2_round = float(input("Enter a float number: "))

# round the user inputed float
rounded_number = round(number_2_round)

# print the rounded number
print(f'{number_2_round} roundd is {rounded_number}')


# Note the round() function will round up or down depending on the decimal value
# but for .5 it will round to the nearest even number so for 2.5 it will round down but for 3.5 it will round up
# this is called bankers rounding and is inaccurate for some applications
