# Ch5Ex4.py
# Ch5Ex4
# Sarah Vigstol
# This program prompts the user for monthly automobile expenses (loan payment,
# insurance, gas, oil, tires, and maintenance), then calculates and displays
# the total monthly and total annual cost of these expensesn.

# Student name must be the first line of output
print('Sarah Vigstol')

# Define function that displays a welcome message to the user at start
def welcome():
    print('Automobile Expenses Calculator')
    print('--------------------')

# Define function that calculates and displays total monthly and annual costs
# based on the user input
def showExpenses(loan, insure, gas, oil, tires, maintenance):
    # Calculate total monthly costs
    totalMonth = loan + insure + gas + oil + tires + maintenance
    # Calculate total annual costs
    totalAnnual = totalMonth * 12

    print(f'''
Loan Payment:\t\t${loan:,.2f}
Insurance:\t\t${insure:,.2f}
Gas:\t\t\t${gas:,.2f}
Oil:\t\t\t${oil:,.2f}
Tires:\t\t\t${tires:,.2f}
Maintenance:\t\t${maintenance:,.2f}
--------------------
Total Monthly Expenses:\t${totalMonth:,.2f}
Total Annual Expenses:\t${totalAnnual:,.2f}
''')

# Call welcome function to display welcome message
welcome()
# Get monthly cost of each type of expense from user and assign each to a new
# variable
loan = float(input('Enter monthly loan payment. $'))
insure = float(input('Enter monthly insurance payment. $'))
gas = float(input('Enter monthly cost of gas. $'))
oil = float(input('Enter monthly cost of oil. $'))
tires = float(input('Enter monthly cost of tires. $'))
maintenance = float(input('Enter monthly maintenance cost. $'))

# Call showExpenses function to calculate and display results
showExpenses(loan, insure, gas, oil, tires, maintenance)

# Program output
'''
Sarah Vigstol
Automobile Expenses Calculator
--------------------
Enter monthly loan payment. $465.00
Enter monthly insurance payment. $150.00
Enter monthly cost of gas. $215.00
Enter monthly cost of oil. $25.00
Enter monthly cost of tires. $10.00
Enter monthly maintenance cost. $12.00

Loan Payment:		$465.00
Insurance:		$150.00
Gas:			$215.00
Oil:			$25.00
Tires:			$10.00
Maintenance:		$12.00
--------------------
Total Monthly Expenses:	$877.00
Total Annual Expenses:	$10,524.00

>>> 
'''
