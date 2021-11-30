# Ch6Ex10B.py
# Ch6Ex10B
# Sarah Vigstol
# This program reads the records from golf.txt and displays them.

# Define main function
def main():

    # Student name must be first line of output
    print('Sarah Vigstol')
 
    # Initialize variables for player names and scores
    name = ''
    golfScore = 0
    count = 0 # Accumulator to track # of lines
    
    # Display welcome message
    print('Springfork Amateur Golf Club')
    print('Tournament Scores')
    print('Getting scores now...\n')

    # Open golf.txt for reading
    infile = open('golf.txt', 'r')

    # Read first name
    name = infile.readline()
    
    # Check for empty string
    # Continue processing as long as an empty string is not returned
    while name != '':
        # Read player score
        golfScore = infile.readline()
        count += 1 # Increase by 1 for each line read
        
        # Strip newlines from name and score fields
        name = name.rstrip('\n')
        golfScore = golfScore.rstrip('\n')
    
        # Display data with one line space between the data 
        # for every two players
        if count % 2 == 0:
            print(f'Name: {name}')
            print(f'Score: {golfScore}\n')
        else:
            print(f'Name: {name}')
            print(f'Score: {golfScore}')
        
        # Read next name
        name = infile.readline()

    # Close file
    infile.close()

# Call the main function.
main()
