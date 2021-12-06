# Ch3Ex10.py
# Ch3Ex10
# Sarah Vigstol
# This program is a change-counting game that prompts the user to enter
# a number of pennies, nickels, dimes, and quarters. The user wins if the
# total value of the coins is equal to 1 dollar. If not, a message
# displays whether the total is greater or less than 1 dollar.

# Student name must be the first line of output
print('Sarah Vigstol')

# Declare the value of each coin as constants
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

# Display welcome message and game objective
print('Welcome to the Change Counting Game.')
print('Let\'s try to make exactly $1 in coins!\n')

# Prompt user for the number of each type of coin
# Assign input for each coin to respective variables
userPenny = int(input('How many pennies? '))
userNickel = int(input('How many nickels? '))
userDime = int(input('How many dimes? '))
userQuarter = int(input('How many quarters? '))

print(f'''
Okay, you entered:
\t* {userPenny} pennies
\t* {userNickel} nickels
\t* {userDime} dimes, and
\t* {userQuarter} quarters
''')


# Add up the total value of the coins entered by the user
# and display appropriate message to user
userTotal = (userPenny * PENNY) + (userNickel * NICKEL) + (userDime * DIME) + (userQuarter * QUARTER)
print(f'Your total is: ${userTotal:.2f}')
# Determine whether or not the total value is equal to 1 dollar
if userTotal > 1:
    print('Too bad, that\'s greater than $1...') # Total too high
elif userTotal < 1:
    print('Too bad, that\'s less than $1...') # Total too low
else:
    print('You won!') # Winner

# Program output
'''
Sarah Vigstol
Welcome to the Change Counting Game.
Let's try to make exactly $1 in coins!

How many pennies? 29
How many nickels? 4
How many dimes? 3
How many quarters? 1

Okay, you entered:
	* 29 pennies
	* 4 nickels
	* 3 dimes, and
	* 1 quarters

Your total is: $1.04
Too bad, that's greater than $1...
>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/Ch3Ex10.py
Sarah Vigstol
Welcome to the Change Counting Game.
Let's try to make exactly $1 in coins!

How many pennies? 15
How many nickels? 2
How many dimes? 2
How many quarters? 1

Okay, you entered:
	* 15 pennies
	* 2 nickels
	* 2 dimes, and
	* 1 quarters

Your total is: $0.70
Too bad, that's less than $1...
>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/Ch3Ex10.py
Sarah Vigstol
Welcome to the Change Counting Game.
Let's try to make exactly $1 in coins!

How many pennies? 20
How many nickels? 11
How many dimes? 0
How many quarters? 1

Okay, you entered:
	* 20 pennies
	* 11 nickels
	* 0 dimes, and
	* 1 quarters

Your total is: $1.00
You won!
'''
