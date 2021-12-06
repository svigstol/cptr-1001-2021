# Ch8Ex7.py
# Ch8Ex7
# Sarah Vigstol
# This program reads the text.txt file and calculates the number of uppercase,
# lowercase, digits and whitespace characters in the file.

# Define main function
def main():

    # Student name should be first line of output
    print ('Sarah Vigstol\n')

    # Display welcome message
    welcome()

    # Declare local variables
    # Each accumulator will track the total number of each character type
    upperCount = 0
    lowerCount = 0
    digitCount = 0
    spaceCount = 0
    
    # Open file text.txt for reading
    infile = open('text.txt', 'r')

    # Read in data from the file
    charList = infile.readlines()

    # Strip newlines from each list item
    for index in range(len(charList)):
        charList[index] = charList[index].rstrip('\n')
        
    # Step through each character in the file. Determine if the character is
    # uppercase, lowercase, a digit, or space, and keep a running total of each. 
    for word in charList:
        for character in word:
            if character.islower():
                lowerCount +=1
            elif character.isupper():
                upperCount += 1
            elif character.isdigit():
                digitCount += 1
            elif character.isspace():
                spaceCount += 1
       
    # Close file
    infile.close()
        
    # Display totals
    print('Here are the totals for this file:')
    print(f'* {upperCount:,} uppercase letters')
    print(f'* {lowerCount:,} lowercase letters')
    print(f'* {digitCount:,} digits, and')
    print(f'* {spaceCount:,} whitespace characters.')

# Define welcome message function
def welcome():
    print('Character Type Counter')
    print('Let\'s see how many of each type are in text.txt...\n')

# Call the main function.
main()


# Program output
'''
Sarah Vigstol

Character Type Counter
Let's see how many of each type are in text.txt...

Here are the totals for this file:
* 29 uppercase letters
* 1,228 lowercase letters
* 30 digits, and
* 250 whitespace characters.
>>> 
'''
