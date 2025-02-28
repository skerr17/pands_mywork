# this program keeps prompting the user for numbers until they enter zero 0
# this program will append these to a list and print them out at the end
# Author: Stephen Kerr

# Prompt the user for a number in a while loop
users_number = int(input("Please Enter a number to memory,\nNote to quit enter Zero.\nEnter a number: "))

# initialise the list
users_numbers_list = []

# append that number to a list
while users_number != 0:
    # adds the user input to the list
    users_numbers_list.append(users_number)  # Found out about list_name.append() method at https://www.w3schools.com/python/python_lists_add.asp
    # requests another number from the user
    users_number = int(input("Please Enter a number to memory,\nNote to quit enter Zero.\nEnter a number: "))

#initalise the total_numbers variable
total_number = sum(users_numbers_list)

'''
# calculate the average value in the list 
for value in users_numbers_list:        # found notes on enumerate at https://www.geeksforgeeks.org/enumerate-in-python/
    # sum the numbers and divide by the index
    total_number += value                       # found out how to add elements of a list using a for loop from here https://pythonguides.com/sum-elements-in-list-in-python-using-for-loop/
    average_number = total_number / len(users_numbers_list)
'''

# more condensed version of calculting the average
average_number = total_number / len(users_numbers_list)


# print out the average value
print(f'The average value of the list is: {average_number}')
print(f'This was calculated by dividing the sum of the numbers entered by the number of enteries: {total_number} / {len(users_numbers_list)}')

# prints the list out 
print(f'You entered the following number: {users_numbers_list}')
for value in users_numbers_list:
    print(value)   

