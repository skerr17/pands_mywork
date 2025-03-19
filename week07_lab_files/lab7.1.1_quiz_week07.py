# This program answers the questions for the Quiz in week 7's lab
# Authoered: Stephen Kerr

# Question 1
# a. What is the output of the following code?
    # the code will open the file (if it exists) 
    # and read its content and print it 

# b. What is the output of the following code? 
# 1) if the files doesn't exist
    # the program will create a new file and write the string  
# 2) what will be outputed to the terminal
    # the code will print 'test b ' 
    # and on a new line 'another line'

# c. what will the contents of file 'test-b.txt' be after the code is run
    # the file will contain the following text
    # test b
    # another line

# d. what will the contents be after ht modification? 
    # 'test b' is changed to 'test d' 

'''
a. The program will throw an error, the default mode is ‘r’ ie read, and read 
will throw an error if the file does not exist. 
b. 7 
13 
This is because the write function returns the number of characters 
writing to the file this includes the new line character, I have not 
tested this on a windows machine(it may be one more). 
c. Another line 
The file will be overwritten when we open the file in write mode 
(again) 
d. test d 
another line 
This time we open the file in append mode, so the file is not 
overwritten 
'''