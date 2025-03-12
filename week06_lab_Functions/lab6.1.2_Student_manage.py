# This program allows the user to create new students and to view students
# Authored by: stephen kerr


# Menu commands to add a student, view students and quit
def displayMenu():
    print('What would you like to do?')
    print('(a) Add  new student')
    print('(v) View')
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

# Main program
# Test the function
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print('\n\nplease select either a, v or q')
    choice = displayMenu()


