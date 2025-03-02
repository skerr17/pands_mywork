# This program puts 10 random numbers into a queue
# the program displays all the numbers in the list 
# And the takes the number at the first position in the queue from the list one at a time, 
# prints it and the current number list
# Auther: Stephen Kerr

# import random module
import random

# intitialis the list
random_number_queue = []

# making the different parameters of the program into easily editable varioables 
length_of_list = 10
# Assumed the random numbers should be between 0 and 100
random_number_range_start = 0
random_number_range_end = 100


# create the list of 10 random numbers 
while len(random_number_queue) < length_of_list:
    random_number_queue.append(random.randint(random_number_range_start, random_number_range_end))

# print the list
print(f'Queue is {random_number_queue}')

# create a while loop to pop the first number from the list until none are left and print out the list
while len(random_number_queue) != 0:
    print(f'Current Number: {random_number_queue.pop(0)} was removed. New queue is {random_number_queue}')