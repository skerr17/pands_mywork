# This program allows the user to create new students and to view students
# Authored by: stephen kerr


# Menu commands to add a student, view students and quit
def displayMenu():
    print('What would you like to do?')
    print('(a) Add  new student')
    print('(v) View')
    print('(s) Save')
    print('(l) Load')
    print('(q) Quit')
    choice = input('Type one letter (a/v/q):')
    return choice


# Function to add students
def doAdd(students):
    # read the student name from the user
    current_student = {}
    current_student['student_name'] = input('Enter student name: ').strip()
    current_student['modules'] = readModules()
    students.append(current_student)


def readModules():
    modules = []
    # read modules and grades from the user with the escape option
    module_name = input('Enter the first module name (\'q\' to quit): ').strip()

    while module_name != 'q':
        module = {}
        module['module_name'] = module_name
        try:
            module['grade'] = int(input('Enter grade: '))
            modules.append(module)
            module_name = input('Enter next module name (\'q\' to quit): ').strip()
        except ValueError:
            print('Please enter a valid grade')
            module['grade'] = int(input('Enter grade: '))
    return modules



# Function to view students
def doView(students):
    for student in students:
        print(f"Student Name: {student['student_name']}")
        for module in student['modules']:
            print(f"\tModule: {module['module_name']}, Grade: {module['grade']}")


# import json
import json 


# function to save the student data to a file
def do_save(students):
    with open('students.json','wt') as f:
        json.dump(students,f)
    print('students saved')


# Function to load the student data from a file
def do_load():
    try:
        with open('students.json','rt') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Main program
# Test the function
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        do_save(students)
    elif choice == 'l':
        students = do_load()
    elif choice != 'q':
        print('\n\nplease select either a, v or q')
    choice = displayMenu()


