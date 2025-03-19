# this code uses the code from last weeks lab 
# with the addiotnal function to save the data to a file
# note sys and os module was used to import the fucntions as a module
# author: Stephen Kerr

# also note the code was changed in the original file and not here directly 



import sys # sys module in python provides a number of functions and variables that can be used to manipulate different parts of the Python runtime environment.
import os # the OS module in Python provides a way of using operating system dependent functionality.

# Add the directory containing the module to the Python path
sys.path.append(os.path.abspath('c:/Users/kerrs/Desktop/pands/pands_mywork/week06_lab_Functions'))

# Import the functions from the module
from lab6_1_2_Student_manage import displayMenu, doAdd, doView, do_save

# Call the displayMenu function
displayMenu()