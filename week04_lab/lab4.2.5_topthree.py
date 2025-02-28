# this program generates 10 random numbers (0-100)
# prints them out then prints out the top three
# Author: Stephen Kerr

import random

# generate 10 random numbers
random_numbers_list = []

while len(random_numbers_list) < 10: 
    # add a random number from 0 to 100
    random_number_generation = random.randint(0,100)
    random_numbers_list.append(random_number_generation)

# identify the top 3 of the 10
# sort the list
random_numbers_list.sort(reverse = True)        # found out how to sort list from https://www.w3schools.com/python/python_lists_sort.asp

# extract the top 3
top_three_random_numbers = random_numbers_list[:3]

# print hte 10 numbers and then top 3
print(f'10 random numbers\t {random_numbers_list}')
print(f'The top 3 are\t\t {top_three_random_numbers}')