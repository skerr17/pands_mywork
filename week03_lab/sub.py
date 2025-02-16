# This program reads in two numbers and subtracts the first one from the second one
# Author: Stephen Kerr

# prompt the user for the first number
# added in ValuEerror handling to catch if the user enters in a float or str
while True: 
    try:
        number_1 = int(input("Enter the first number: "))
        number_1
        break
    except ValueError: 
        print("You have entered an invalid value for the first number, please enter a number (integer): ")

# prompt the user for the second number
# added in ValuEerror handling to catch if the user enters in a float or str
while True: 
    try:
        number_2 = int(input("Enter the second number: "))
        number_2
        break
    except ValueError: 
        print("You have entered an invalid value for the second, please enter a number (integer): ")

print("Thank you for entering the numbers")

# subtract the first number from the second number
answer = number_2 - number_1

# prints answer to the console
print(f'The answer of {number_2} - {number_1} = {answer}')


# if you enter in a float or str that will cause and error so error handling needs to be added to this code to hanle that 
# error = ValueError

# Found a decenct explaination here: 'https://www.geeksforgeeks.org/input-validation-in-python/'

