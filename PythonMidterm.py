# PythonMidterm.py
# Python Midterm Assessment Project
# Sarah Vigstol
# This program gets hours worked and rate of pay from the user, then computes
# and displays gross pay, taxes, and net pay. Any time worked beyond 50 hours
# is calculated at double time, and time worked beyond 40 but less than 50
# hours are calculated at time and a half.

# Student name is the first line of output
print('Sarah Vigstol')

# Define welcome function that displays a welcome message to the user
def welcome():
    print('Python Midterm Assessment Project')
    print('Paycheck Calculator')
    print('--------------------')

# Display welcome message    
welcome()
# Prompt user for hours worked and rate of pay, then assign values to new
# variables as an integer and a float, respectively
hoursWorked = int(input('Enter the hours worked: '))
rateOfPay = float(input('Enter the rate of pay: $'))

# Define function that calculates gross pay from user input
def calcGross(hoursWorked):
    # Define new constant for max hours paid out at regular rate of pay
    REGULARHOURS = 40
    # Define new constant for min hours paid out at double rate of pay
    DOUBLEHOURS = 50
    # Define constants for time and a half and double time rates of pay
    TIMEANDAHALF = 1.5
    DOUBLETIME = 2

    # Determine pay based on the number of hours worked and return the result
    # to the program
    if hoursWorked > 40 and hoursWorked < 50:
        # Calculate hours and pay at time and a half
        overtimeHours = hoursWorked - REGULARHOURS
        overtimePay = overtimeHours * (rateOfPay * TIMEANDAHALF)
        # Calculate gross pay
        gross = (REGULARHOURS * rateOfPay) + overtimePay
        return gross
    elif hoursWorked >= 50:
        # Calculate hours and pay at time and a half
        overtimeHours = 10
        overtimePay = overtimeHours * (rateOfPay * TIMEANDAHALF)
        # Calculate hours and pay at double time
        doubletimeHours = hoursWorked - DOUBLEHOURS
        doubletimePay = doubletimeHours * (rateOfPay * DOUBLETIME)
        # Calculate gross pay
        gross = (REGULARHOURS * rateOfPay) + overtimePay + doubletimePay
        return gross
    else:
        # Calculate gross pay
        gross = hoursWorked * rateOfPay
        return gross

# Define function that calculates taxes based on the value of grossPay and
# return the result to the program
def calcTax(grossPay):
    # Define constants for the rates of each type of tax
    FEDERALTAX = 0.25
    MNSTATETAX = 0.07
    SOCIALSECURITY = 0.06
    MEDICARE = 0.02
    # Calculate total tax paid
    tax = (grossPay * FEDERALTAX) + (grossPay * MNSTATETAX) + (grossPay * SOCIALSECURITY) + (grossPay * MEDICARE)
    return tax

# Call calcGross function and return result to grossPay variable
grossPay = calcGross(hoursWorked)
# Call calcTax function and return result to taxesPaid variable
taxesPaid = calcTax(grossPay)
# Calculate net pay from previous two variables and assign to new variable
netPay = grossPay - taxesPaid

# Display gross pay, taxes paid, and net pay
print(f'''
The gross pay is: ${grossPay:0.2f}
The taxes are: ${taxesPaid:0.2f}
The net pay is: ${netPay:0.2f}
''')


# Program output
'''
Sarah Vigstol
Python Midterm Assessment Project
Paycheck Calculator
--------------------
Enter the hours worked: 55
Enter the rate of pay: $15.50

The gross pay is: $1007.50
The taxes are: $403.00
The net pay is: $604.50

>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/PythonMidterm.py
Sarah Vigstol
Python Midterm Assessment Project
Paycheck Calculator
--------------------
Enter the hours worked: 45
Enter the rate of pay: $20.75

The gross pay is: $985.62
The taxes are: $394.25
The net pay is: $591.38

>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/PythonMidterm.py
Sarah Vigstol
Python Midterm Assessment Project
Paycheck Calculator
--------------------
Enter the hours worked: 40
Enter the rate of pay: $10.00

The gross pay is: $400.00
The taxes are: $160.00
The net pay is: $240.00

>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/PythonMidterm.py
Sarah Vigstol
Python Midterm Assessment Project
Paycheck Calculator
--------------------
Enter the hours worked: 35
Enter the rate of pay: $10.00

The gross pay is: $350.00
The taxes are: $140.00
The net pay is: $210.00

>>> 
'''
