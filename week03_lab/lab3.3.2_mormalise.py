# this program reads in a string and strips any leading or trailling spaces, it also converts all the letters to lower case
# The program also outputs the lenght of the original string and the normalised one
# Author: Stephen Kerr

# prompt the user for a string
raw_string = str(input('Please enter a string: '))

# normalise the string
normalised_string = raw_string.strip().lower()

# calculate the lenght of the original string
raw_string_lenght = len(raw_string)

# calculate the lenght of the normalised string
normalised_string_lenght = len(normalised_string)

# output the normalised string
print(f'You inputted: {raw_string}, which has a lenght of {raw_string_lenght}.')
print(f'The normalised version of your string is: {normalised_string}, which has a lenght of {normalised_string_lenght}.')