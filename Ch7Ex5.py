# Ch7Ex5.py
# Ch7Ex5
# Sarah Vigstol
# This program reads the file charge_accounts.txt into a list. It then asks the
# user to enter a charge account number. The program should determine if the 
# number is valid; if not, provide the appropriate error message.

def main():

    # Student name should be first line of output
    print('Sarah Vigstol')

    # Display welcome message
    welcome()

    try:
        # Open charge_accounts.txt for reading
        infile = open('charge_accounts.txt', 'r')

        # Read the contents of the file into a list
        accountList = infile.readlines()

        # Close the file
        infile.close()

        # Strip newlines from each element
        for index in range(len(accountList)):
            accountList[index] = accountList[index].rstrip('\n')

        # Prompt user for account number
        userNumber = input('Please enter a seven-digit account number. ')

        # Use in operator to search for the account specified by user
        if userNumber not in accountList:
            print(f'Account number {userNumber} is INVALID.')
        else:
            print(f'Account number {userNumber} is VALID.')
            
    # Exception handlers
    except IOError: # File is missing
        print('An error occurred while attempting to read charge_accounts.txt.')
        print('Check that the file is located in the correct directory and try again.')
    except: # All other exceptions
        print('An error occurred.')

# Define welcome message function
def welcome():
    print('Company XYZ Charge Account Validator')
    print('Getting account numbers...\n')

# Call the main function
main()


# Program Output - Run 1
'''
Sarah Vigstol
Company XYZ Charge Account Validator
Getting account numbers...

Please enter a seven-digit account number. 5552012
Account number 5552012 is VALID.
>>> 
'''

# Program Output - Run 2
'''
Sarah Vigstol
Company XYZ Charge Account Validator
Getting account numbers...

Please enter a seven-digit account number. 1234567
Account number 1234567 is INVALID.
>>> 
'''
