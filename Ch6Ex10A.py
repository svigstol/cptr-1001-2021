# Ch6Ex10A.py
# Ch6Ex10A
# Sarah Vigstol
# This program inputs a golf player's name and score from the keyboard
# and stores the data into a file named golf.txt

# Define main function
def main():
    # Student name must be first line out output
    print('Sarah Vigstol')

    # Define variables for player name, score, and total number of players
    name = ''
    golfScore = 0
    numPlayers = 0

    # Display welcome message
    print('Springfork Amateur Golf Club')
    print('Tournament Scores\n')
    # Prompt user for the number of players
    numPlayers = int(input('Enter the number of players in the tournament: '))
    
    # Open golf.txt for writing
    outfile = open('golf.txt', 'w')

    # Write data to file
    for player in range(numPlayers):
        name = input('Enter the name of the player: ')
        golfScore = input('Enter the golf score: ')

        outfile.write(name + '\n' + golfScore + '\n')

    # Display confirmation that input has been written to golf.txt
    print(str(numPlayers) + ' players\' scores have been saved to golf.txt')
    print('Closing file...')

    # Close file
    outfile.close()

# Call the main function
main()
