# Employee class
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
