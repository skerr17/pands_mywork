# This program stores a student name and a list of her courses and grades in a dictionary
# Note the number of courses she has could change
# Auther: Stephen Kerr

# References: 
# Used W3schools - Here https://www.w3schools.com/python/python_dictionaries.asp
# Found a good artical on "how to add user inputs to a dictionary" - Here https://www.geeksforgeeks.org/how-to-add-user-input-to-a-dictionary-in-python/

# read the student name from the user
student_name = input('Hello Student, \nPlease enter your name: ')

# Initials the modules dictionary 
modules_dict = {}

# read the course names and grades to the modules dictionary from the user in a while loop 
# with an escape option 
while True:
    # prompt the user for a course
    course_name = input('Enter \'q\' to quit the program at anytime when you have entered all your Modules and Grades,'
                       '\nPlease provide the name of your course: ')
    if course_name == 'q':
        # To not have 'q' in the modules_dict
        break
    # prompt the user for a grade 
    grade = int(input(f'What is your current grade in {course_name} : '))  
    # save that course names and grades to the modules dictionary
    modules_dict[course_name] = int (grade)

print(modules_dict)

# create the dictionary to store the student data and save the user inputs to
student_data = {
    'name': student_name,
    'modules': modules_dict,
}

# print the student entered data of their name and modules + grades
print(student_data)

# Note I did all this without realising the questions was just asking to print prompt the user but anyhow 

print(f'Student: {student_data["name"].capitalize()}')
for course_name, grade in student_data['modules'].items():
    print(f'\t{course_name.capitalize()} : {grade}') 
