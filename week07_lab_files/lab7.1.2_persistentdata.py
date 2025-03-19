# This program reads the number of times it has been run
# using a file to store the number of times it has been run
# and print the number of times it has been run
# Auther: Stephen Kerr


FILENAME = "lab7.1.2_count.txt"

# function reads the number from the file
def readNumber():
    with open(FILENAME, "rt") as f:
        number = int(f.read())
        return number


# function writes the number to the file
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number)) # note write takes the a string


num = readNumber() # reads what is in the count.txt file
num += 1 # adds 1 everytime the code is run
writeNumber(num) # writes the new number to the file
print(f'This program has been run {num} times.')
