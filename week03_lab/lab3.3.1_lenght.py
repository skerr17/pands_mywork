# this program reads a string an outputs the length of the string
# Also includes the answer to question 2 of Lab 3.3.2
# Author: Stephen Kerr

# Prompt the user for a string 
input_string = str(input("Enter a string: "))

# calculate the lenght of the string
string_lenght = len(input_string)

# print the lenght of the string out
print(f"The lenght of the string \"{input_string}\" is {string_lenght}")



# Question 2 of Lab 3.3.2
# How would you output a string like this?
#John said   "hi"
# I said     "bye"

# Answer: by using the escape character \ before the double quotes
print('John said \t"hi"\nI said\t\t"bye"')