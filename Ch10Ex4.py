# Ch10Ex4.py
# Ch10Ex4
# Sarah Vigstol
# This program will create three Employee objects and then display the data in each.

# Import employee class
import emp

# Define main function
def main():
    # Call welcome function
    welcome()

    # Create three instances of Employee class
    emp1 = emp.Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    emp2 = emp.Employee('Mark Jones', '39119', 'IT', 'Programmer')
    emp3 = emp.Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    # Display employee 1 data
    print('Employee 1:')
    print('------------')
    print(emp1)
    print()
    # Display employee 2 data
    print('Employee 2:')
    print('------------')
    print(emp2)
    print()
    # Display employee 3 data
    print('Employee 3:')
    print('------------')
    print(emp3)

# Define welcome message function
def welcome():
    # Student name must be first line of output
    print('Sarah Vigstol\n')

# Call main function
main()


# Program output
'''
Sarah Vigstol

Employee 1:
------------
Name: Susan Meyers
ID Number: 47899
Department: Accounting
Job Title: Vice President


Employee 2:
------------
Name: Mark Jones
ID Number: 39119
Department: IT
Job Title: Programmer


Employee 3:
------------
Name: Joy Rogers
ID Number: 81774
Department: Manufacturing
Job Title: Engineer

>>>
'''

# Employee class
'''
class Employee:
    # Initialize employee attributes
    def __init__(self, name, idNumber, department, title):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__title = title

    # Accepts an argument for employee name
    def setName(self, name):
        self.__name = name

    # Accepts an argument for employee id
    def setIdNumber(self, idNumber):
        self.__idNumber = idNumber

    # Accepts an argument for employee department
    def setDepartment(self, department):
        self.__department = department

    # Accepts an argument for employee title
    def setTitle(self, title):
        self.__title = title

    # Returns employee name
    def getName(self):
        return self.name

    # Returns employee id number
    def getIdNumber(self):
        return self.id_number

    # Returns employee department
    def getDepartment(self):
        return self.department

    # Returns employee title
    def getTitle(self):
        return self.title

    # Returns employee object's state as a string
    def __str__(self):
        result = f'Name: {self.__name}\n' + \
        f'ID Number: {self.__idNumber}\n' + \
        f'Department: {self.__department}\n' + \
        f'Job Title: {self.__title}\n'

        return result
'''
