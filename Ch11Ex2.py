# Ch11Ex2.py
# Ch11Ex2
# Sarah Vigstol
# This program creates a ShiftSupervisor object, prompts the user for attribute data, then displays the entered data

# Import module
import empex11

# Define main function
def main():
    # Call welcome function
    welcome()

    # Local variables
    workerName= ''
    workerId = ''
    workerSalary = 0.0
    workerBonus = 0.0

    # Get data attributes
    workerName = input('Enter worker name: ')
    workerId = input('Enter worker ID number: ')
    workerSalary = float(input('Enter annual salary: '))
    workerBonus = float(input('Enter production bonus: '))

    # Create an instance of ShiftSupervisor
    worker = empex11.ShiftSupervisor(workerName, workerId, \
                                  workerSalary, workerBonus)

    # Display supervisor information
    print()
    print('Shift Supervisor Profile:')
    print('--------------------------')
    print('Name:', worker.get_name())
    print('ID Number:', worker.get_idNumber())
    print('Annual Salary: $', \
           format(worker.get_annualSalary(), ',.2f'), sep='')
    print('Production Bonus: $', \
           format(worker.get_bonus(), ',.2f'), sep='')

# Define welcome message function
def welcome():
    # Student name must be first line of output
    print('Sarah Vigstol')
    print()

# Call main function
main()


# Program output
'''
========== RESTART: C:\Users\Lutefisk\github\cptr-1001-2021\Ch11Ex2.py =========
Sarah Vigstol

Enter worker name: James Smith
Enter worker ID number: 2468
Enter annual salary: 97531.55
Enter production bonus: 5000

Shift Supervisor Profile:
--------------------------
Name: James Smith
ID Number: 2468
Annual Salary: $97,531.55
Production Bonus: $5,000.00
'''

# Employee class
'''
class Employee:
    def __init__(self, name, idNumber):
        # Initialize name and idNumber attributes
        self.__name = name
        self.__idNumber = idNumber

    # Setters for name and idNumber attributes
    def set_name(self, name):
        self.__name = name

    def set_idNumber(self, idNumber):
        self.__idNumber = idNumber

    # Getters for name and idNumber attributes
    def get_name(self):
        return self.__name

    def get_idNumber(self):
        return self.__idNumber

# ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, name, idNumber, shiftNumber, payRate):
        # Call superclass __init__ method
        Employee.__init__(self, name, idNumber)

        # Initialize shiftNumber and payRate attributes
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate

    # Setters for shiftNumber and payRate
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber

    def set_payRate(self, payRate):
        self.__payRate = payRate

    # Getters for shiftNumber and payRate
    def get_shiftNumber(self):
        return self.__shiftNumber

    def get_payRate(self):
        return self.__payRate

# ShiftSupervisor subclass
class ShiftSupervisor(Employee):
    def __init__(self, name, idNumber, annualSalary, bonus):
        # Call superclass __init__ method
        Employee.__init__(self, name, idNumber)

        # Initialize annualSalary and bonus attributes
        self.__annualSalary = annualSalary
        self.__bonus = bonus

    # Setters for annualSalary and bonus attributes
    def set_annualSalary(self, annualSalary):
        self.__annualSalary = annualSalary

    def set_bonus(self, bonus):
        self.__bonus = __bonus

    # Getters for annualSalary and bonus attributes
    def get_annualSalary(self):
        return self.__annualSalary

    def get_bonus(self):
        return self.__bonus
'''


