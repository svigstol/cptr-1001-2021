class Employee:
    def __init__(self, name, idNumber):
        # Initialize name and idNumber attributes
        self.__name = name
        self.__id_number = idNumber

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
