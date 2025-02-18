# this program prints out a random fruit

# import the random module
import random

# fruits list
fruits = ['Apple', 'Orange', 'Banana', 'Pinapple', 'strawberry']

# generate a random number between 0 and the lenght of the fruits list - 1
index = random.randint(0, len(fruits)-1)

print(f'A Random Fruit: {fruits[index]}')