# This program answers Q1 of week 5 Lab sheet
# Author: Stephen Kerr

'''
Questions
What are the variable types of the following variables in the code above
a. numberOfQuestions 
b. averageAge
c. debugMode
d. name
e. ages
f. months
g. months[1]
h. book
i. stuff
j. stuff[2]
k. someone
l. someone["firstname"]
m. me
n. me["teaching"]
o. me["teaching"][0]["semester"]
p is a trick question look at it carefully
p. me["teaching"][0]["coursename"]
'''

# a numberOfQuestions = Integer
# b average = Float
# c debugMode = Boolean
# d name = String
# e ages = List
# f months = Tuple
# g months[1] = String == 'feb'
# h book = Dictionary
# i stuff = List
# j stuff[2] = Boolean == False
# k someone = Dictionary
# l someone["firstname"] = String == 'joe'
# m me = Dictionary
# n me["teaching"] = List
# o me["teaching"][0]["semester"] = Int == 1
# p is a trick question as there will be a syntax error as there is no key "coursename" in the dictionary
someone = dict(firstname="joe")
print(type(someone))