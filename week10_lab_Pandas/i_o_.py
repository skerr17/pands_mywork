# This program contains daa 
# Author: Stephen Kerr

import pandas as pd

list_data= [
['John', 'math', 45],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61],
['Alice', 'history' , 97],
]
df = pd.DataFrame(list_data, columns=['name','subject','grade'])
# print(df.head(3))


#using the describe method to get a summary of the data
#print(df.describe())

# get stats of each subject 
#print(df.groupby('subject').describe())

# get stats of each name
#print(df.groupby('name').describe())

# write the data to a csv file
df.to_csv('grades.csv')

# The reason the 
# The reason the file starts with a comma is because the 'to_csv' method adds a header row by default, and the first column is the index column.

# write the data to an excel file without the index column
df.to_excel('grades.xlsx', index=False, sheet_name='data')


# calculate the mean of the grades
mean = df.describe().loc['mean']
print(mean)

mean_other = df['grade'].mean()
print(mean_other)