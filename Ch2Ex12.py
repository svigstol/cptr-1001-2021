# Ch2Ex12.py
# Ch2Ex12
# Sarah Vigstol
# This program calculates and displays the amounts for which Joe purchased
# and sold stock, commission fees for both transactions, and the total
# amount remaining after sale.

# Student name must be the first line of output
print('Sarah Vigstol')

# Declare constants for number of shares, commission percent, and values per
# share at purchase and at sale
SHARES = 2000
COMMISSION_PERCENT = 3
PURCHASE_VALUE = 40.00
SALE_VALUE = 42.75

# Calculate total amount paid for stock and assign to total_paid variable
total_paid = SHARES * PURCHASE_VALUE
# Calculate commission paid at purchase and assign to purchase_commission
# variable
purchase_commission = total_paid * (COMMISSION_PERCENT * 0.01)

# Calculate the total amount received for sale of the stock and assign to
# total_received variable
total_received = SHARES * SALE_VALUE
# Calculate commission paid at sale and assign to
# sale_commission variable
sale_commission = total_received * (COMMISSION_PERCENT * 0.01)

# Calculate the total commission paid and assign to
# total_commission variable
total_commission = purchase_commission + sale_commission

# Calculate the amount remaining after both transactions
total_remaining = total_received - (total_paid + total_commission)

# Display details of Joe's original purchase including the total
# amount paid and commission paid
print(f'''
Last month, Joe purchased some stock in Acme Software, Inc.
Here are the details of the purchase:\n
\t* Shares Purchased: {SHARES:,} @ ${PURCHASE_VALUE:.2f}/ea
\t* Commission Rate: {COMMISSION_PERCENT}%\n
\tSubtotals:
\t* Stock: ${total_paid:,.2f}
\t* Commission: ${purchase_commission:,.2f}
''')

# Display details of Joe's sale of the stock including the total
# amount received and commission paid
print(f'''
Two weeks later, Joe sold the stock.
Here are the details of the sale:\n
\t* Shares Sold: {SHARES:,} @ ${SALE_VALUE}/ea
\t* Commission Rate: {COMMISSION_PERCENT}%\n
\tSubtotals:
\t* Stock: ${total_received:,.2f}
\t* Commission: ${sale_commission:,.2f}

''')
# Display total remaining after commission has been paid
print(f'After paying his broker, Joe has a total of ${total_remaining:,.2f} left over from his sale.')

'''
Sarah Vigstol

Last month, Joe purchased some stock in Acme Software, Inc.
Here are the details of the purchase:

	* Shares Purchased: 2,000 @ $40.00/ea
	* Commission Rate: 3%

	Subtotals:
	* Stock: $80,000.00
	* Commission: $2,400.00


Two weeks later, Joe sold the stock.
Here are the details of the sale:

	* Shares Sold: 2,000 @ $42.75/ea
	* Commission Rate: 3%

	Subtotals:
	* Stock: $85,500.00
	* Commission: $2,565.00


After paying his broker, Joe has a total of $535.00 left over from his sale.
'''
