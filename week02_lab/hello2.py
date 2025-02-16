# hello2.py
# reads in a person's name and prints out hellp that person
# author: Stephen Kerr

'''
name = input('Enter your name: ')
print('hello ' + name)
'''

# if the space was missing on the print statement after hello then the name would be concatonated to the word hello

# Note \n is a newline character

name = input('Enter your name: ')
# print('Hello ' + name + '\nNice to meet you')

# print('Hello {}\nNice to meet you'.format(name)) # format method
# Also added in the capitalize method to capitalise the first letter of the name

print(f'Hello {name.capitalize()}\nNice to meet you') # f string