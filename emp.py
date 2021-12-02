# Employee class
class Employee:
    # Initialize employee attributes
    def __init__(self, name, id_number, department, title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self._title = title

    # Accepts an argument for employee name
    def set_name(self, name):
        self.__name = name

    # Accepts an argument for employee id
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Accepts an argument for employee department
    def set_department(self, department):
        self.__department = department

    # Accepts an argument for employee title
    def set_title(self, title):
        self._title = title

    # Returns employee name
    def get_name(self):
        return self.__name

    # Returns employee id number
    def get_id_number(self):
        return self.__id_number

    # Returns employee department
    def get_department(self):
        return self.__department

    # Returns employee title
    def get_title(self):
        return self.__title

    # Returns employee object's state as a string
    def __str__(self):
        result = 



        return result
