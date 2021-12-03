# Employee class
class Employee:
    # Initialize employee attributes
    def __init__(self, name, id_number, department, title):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.title = title

    # Accepts an argument for employee name
    def setName(self, name):
        self.name = name

    # Accepts an argument for employee id
    def setIdNumber(self, idNumber):
        self.idNumber = idNumber

    # Accepts an argument for employee department
    def setDepartment(self, department):
        self.department = department

    # Accepts an argument for employee title
    def setTitle(self, title):
        self.title = title

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
        result =

        return result
