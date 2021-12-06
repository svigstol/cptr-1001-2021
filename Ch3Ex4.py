# Ch3Ex4.py
# Ch3Ex4
# Sarah Vigstol
# This program prompts the user for a number within the range of 1 through
# 10, then displays the corresponding Roman numeral. If the input is not a
# valid number, displays an error message.

# Student name must be the first line of output
print('Sarah Vigstol')

# Display welcome message
print('Welcome to the Roman Numeral Convert-O-Matic!')
# Prompt user for a number within the range of 1 through 10
# Assign the input to the userNumber variable
userNumber = input('Please enter a number from 1 to 10:\n>>> ')

# Determine the correct Roman numeral for userNumber using an if statement,
# then display the result
if userNumber == '1':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: I')
elif userNumber == '2':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: II')
elif userNumber == '3':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: III')
elif userNumber == '4':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: IV')
elif userNumber == '5':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: V')
elif userNumber == '6':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: VI')
elif userNumber == '7':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: VII')
elif userNumber == '8':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: VIII')
elif userNumber == '9':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: IX')
elif userNumber == '10':
    print(f'You entered: {userNumber}')
    print('In Roman numerals, this would be: X')
else:
    print(f'D\'oh! \'{userNumber}\' isn\'t a number from 1 to 10!') # Error message

# Program output
'''
Sarah Vigstol
Welcome to the Roman Numeral Convert-O-Matic!
Please enter a number from 1 to 10:
>>>8
You entered: 8
In Roman numerals, this would be: VIII
>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/Ch3Ex4.py
Sarah Vigstol
Welcome to the Roman Numeral Convert-O-Matic!
Please enter a number from 1 to 10:
>>> 9
You entered: 9
In Roman numerals, this would be: IX
>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/Ch3Ex4.py
Sarah Vigstol
Welcome to the Roman Numeral Convert-O-Matic!
Please enter a number from 1 to 10:
>>> 65
D'oh! '65' isn't a number from 1 to 10!
'''
