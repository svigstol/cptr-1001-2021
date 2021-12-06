# Ch2Ex8.py
# Ch2Ex8
# Sarah Vigstol
# This program prompts the user for the cost of food ordered at a restaurant,
# calculates tip and sales tax, then displays each subtotal and the total bill.

# Student name must be the first line of output
print('Sarah Vigstol')

# Prompt user for the food subtotal
print('Please enter the total cost of the food ordered.')
print('An 18% tip and 7% sales tax will be added.')

# Convert the subtotal from a string to a float and assign the value to a new variable
mealSubtotal = float(input('$'))

# Assign a value of 18% to the tip constant
TIP = 0.18
# Assign a value of 7% to the tax constant
TAX = 0.07

# Calculate actual tip and sales tax for the user's subtotal
# Assign the new values to the tipSubtotal and taxSubtotal variables, respectively
tipSubtotal = mealSubtotal * TIP
taxSubtotal = mealSubtotal * TAX

# Calculate the total bill and assign the result to the 'total' variable
# The round function is used to prevent rounding errors as a result of
# binary floating point arithmetic
total = mealSubtotal + round(tipSubtotal, 2) + round(taxSubtotal,2)

# Display the user's original subtotal
# Format to two decimal places if the subtotal was originally a whole value
print(f'You entered a subtotal of: ${mealSubtotal:.2f}')

# Display tip and tax subtotals to the nearest cent
print(f'Tip: ${tipSubtotal:.2f}')
print(f'Sales Tax: ${taxSubtotal:.2f}')
# Display the total bill to the nearest cent
print(f'Your total bill is: ${total:.2f}')

"""
Sarah Vigstol
Please enter the total cost of the food ordered.
An 18% tip and 7% sales tax will be added.
$113.74
You entered a subtotal of: $113.74
Tip: $20.47
Sales Tax: $7.96
Your total bill is: $142.17
"""
