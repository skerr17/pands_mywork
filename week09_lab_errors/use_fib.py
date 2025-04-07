# this program used the module my_functions.py
# to prompt the user for a number and will return the list of Fibonacci sequence
# Author: Stephen Kerr



# impor the module from my_functions.py
import my_functions

n_times = int(input('How many Fibonacci numbers do you want? '))
print(my_functions.fibonacci(n_times))