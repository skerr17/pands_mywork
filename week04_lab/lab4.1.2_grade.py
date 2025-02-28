# asks the user for their grade and will tell the student based on the number % shared the correponding grade
# Author: Stephen Kerr


# impot math to get the .ceil() method
import math

'''
# Basic answer
# ask for a number grade %
percentage_grade = int(input('Please enter your percentage grade here: '))  
# checks what the given % corresponds to and prints out the grade
if percentage_grade < 0 or percentage_grade > 100:
    print(f'{percentage_grade} is not a valide grade.')
elif percentage_grade < 40:
    # Failed grade < 40
    print(f'Sorry you failed with a grade of: {percentage_grade}') 
elif percentage_grade < 50:
    # Pass grade between 40 and 49
    print(f'You passed the with a grade of: {percentage_grade}')
elif percentage_grade < 60:
    # Merit grade between 50 and 59
    print(f'You got a Merit 2 withh a grade of: {percentage_grade}')
elif percentage_grade <70:
    # Merit grade between 60 and 69
    print(f'You got a Merit 2 withh a grade of: {percentage_grade}')
else:
    # Distinction grade above 70 
    print(f'You got a Distinction withh a grade of: {percentage_grade}')
'''

# Q3 code that can hanle a float value and round up
# ask for a number grade %
# can accept a float
# seen the ceil() method at https://www.w3schools.com/python/python_math.asp

percentage_grade_float = float(input('Please enter your percentage grade here: '))

# round the float percentage up to nearest int
percentage_grade = math.ceil(percentage_grade_float)

# checks what the given % corresponds to and prints out the grade
if percentage_grade < 0 or percentage_grade > 100:
    print(f'{percentage_grade} is not a valide grade.')
elif percentage_grade < 40:
    # Failed grade < 40
    print(f'Sorry you failed with a grade of: {percentage_grade}') 
elif percentage_grade < 50:
    # Pass grade between 40 and 49
    print(f'You passed the with a grade of: {percentage_grade}')
elif percentage_grade < 60:
    # Merit grade between 50 and 59
    print(f'You got a Merit 2 withh a grade of: {percentage_grade}')
elif percentage_grade <70:
    # Merit grade between 60 and 69
    print(f'You got a Merit 2 withh a grade of: {percentage_grade}')
else:
    # Distinction grade above 70 
    print(f'You got a Distinction withh a grade of: {percentage_grade}')