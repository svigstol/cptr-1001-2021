# Ch7Ex10.py
# Ch7Ex10
# Sarah Vigstol
# This program reads the file WorldSeriesWinners.txt into a list. The user is then prompted to
# enter a team name. If the team is in the list, display the number of World Series wins for 
# that team between 1903 and 2009.

def main():

    # Student name should be first line of output
    print('Sarah Vigstol')

    # Display welcome message
    welcome()

    # Initialize accumulator
    count = 0

    try:
        # Open WorldSeriesWinners.txt for reading
        infile = open('WorldSeriesWinners.txt', 'r')

        # Read the contents of the file into a list
        teams = infile.readlines()

        # Close the file
        infile.close()

        # Strip newlines from each element
        for index in range(len(teams)):
            teams[index] = teams[index].rstrip('\n')

        # Prompt user for a team
        userTeam = input('Enter a team name: ')

        # Use in operator to search for the team specified by user
        if userTeam not in teams:
            print(f'{userTeam} was not found.')
        else:
            # Step through the list, counting number of times user's team appears
            for listItem in teams:
                if userTeam == listItem:
                    count += 1
            print(f'The {userTeam} have won the World Series {count} time(s)')
            print('in this time period.')
            
    # Exception handlers
    except IOError: # File is missing
        print('An error occurred while attempting to read WorldSeriesWinners.txt.')
        print('Check that the file is located in the correct directory and try again.')
    except: # All other exceptions
        print('An error occurred.')

# Define welcome message function
def welcome():
    print('World Series Champions')
    print('1903 through 2009')
    print('Getting data...\n')

# Call the main function
main()


# Program Output - Run 1
'''
Sarah Vigstol
World Series Champions
1903 through 2009
Getting data...

Enter a team name: Minnesota Twins
The Minnesota Twins have won the World Series 2 time(s)
in this time period.
>>> 
'''

# Program Output - Run 2
'''
Sarah Vigstol
World Series Champions
1903 through 2009
Getting data...

Enter a team name: Boston Red Sox
The Boston Red Sox have won the World Series 6 time(s)
in this time period.
'''
