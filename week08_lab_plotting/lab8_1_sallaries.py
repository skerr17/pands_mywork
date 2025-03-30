# this program makes a list of random salaries
# between two perdefined numbers
# author: Stephen Kerr


# import numpy
import numpy as np

# set ranges and lenght of list
lenght_of_list = 10
min_salary = 20000
max_salary = 80000

# set a random seed # Q2 asked for the seaeding 
np.random.seed(12)

# generate random salaries
salaries = np.random.randint(min_salary, max_salary, lenght_of_list)

# Q3 add another array of numbers that has the 
# same salaries plus 5000
salaries_plus_5000 = salaries + 5000

# Q4 increases all the salaries by 5%
salaries_increase_5_percent = salaries *1.05

# turn this into an import module so moved all 
# the code into a code block for testing 
# (only runs when this file is executed directly)

if __name__ == "__main__":
    # print the list of salaries
    print(f'List of random salaries: {salaries}')
    # print the list of salaries plus 
    print(f'List of random salaries plus 5000: {salaries_plus_5000}')
    # print the list of salaries increased by 5%
    print(f'List of random salaries increased by 5%: {salaries_increase_5_percent}')
