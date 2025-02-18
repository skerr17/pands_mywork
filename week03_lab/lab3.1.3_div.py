# This program reads two numbers and divides the first one by the second and gives the integer result and the remainder
# author: Stephen Kerr

# prompt the user for the first number 
# note will added the ValeuError handling learned from the previous task in sub.py to catch if the user enters in a float or str

while True: 
    try: 
        number_1 = int(input("Enter the first number: "))
        number_1
        break
    except ValueError:
        print("You have entered an invalid value for the first number, please enter a number (integer): ")


# prompt the user for the second number
while True: 
    try: 
        number_2 = int(input("Enter the second number: "))
        number_2
        break
    except ValueError:
        print("You have entered an invalid value for the second number, please enter a number (integer): ")

# divide the first number by the second number and print result to the console
answer = number_1 // number_2
remainder = number_1 % number_2

print(f'The answer of {number_1} divided by {number_2} = {answer} with a remainder of {remainder}')

