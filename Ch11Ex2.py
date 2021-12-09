# Ch11Ex2.py
# Ch11Ex2
# Sarah Vigstol
# Program description

# Import module
import empex11

# Define main function
def main():
    # Call welcome function
    welcome()

    # Local variables
    workerName= ''
    workerId = ''
    workerShift = 0
    workerPay = 0.0

    # Get data attributes
    workerName = input('Enter worker name: ')
    workerId = input('Enter worker ID number: ')
    workerShift = int(input('Enter shift number: '))
    workerPay = float(input('Enter hourly pay rate: '))

    # Create an instance of ProductionWorker
    worker = empex11.ProductionWorker(workerName, workerId, \
                                  workerShift, workerPay)

    # Display worker information
    print()
    print('Production Worker Profile:')
    print('--------------------------')
    print('Name:', worker.get_name())
    print('ID number:', worker.get_idNumber())
    print('Shift:', worker.get_shiftNumber())
    print('Hourly Pay Rate: $', \
           format(worker.get_payRate(), ',.2f'), sep='')

# Define welcome message function
def welcome():
    # Student name must be first line of output
    print('Sarah Vigstol')
    print()

# Call main function
main()


# Program output
'''
# Employee class
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
'''
