# this program takes in a float amount of dollars and returns the absolute amount in cents
# author: Stephen Kerr

# prompt the user for a dollar amount
input_dollars = float(input("Enter a dollar amount: "))

# convert that dollar amount to the absolute value in cents 
abs_cent_amount = int(abs(input_dollars) * 100)

# print out the abosulte amount in cents
print(f'${input_dollars} amount in cents is {abs_cent_amount} cents')