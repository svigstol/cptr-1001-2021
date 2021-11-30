# Ch9Ex1.py
# Ch9Ex1
# Sarah Vigstol
# This program creates a dictionary containing course numbers and the rooms
# numbers of the rooms where the courses meet, a dictionary containing course
# numbers and the names of the instructors that teach the course and a dictionary
# of the meeting times of each course. The program should let the user enter
# the course number then display the course's room number, instructor and meeting time.

# Define main function
def main():
    # Initialize dictionaries
    rooms = {'CS101':'3004',
             'CS102':'4501',
             'CS103':'6755',
             'NT110':'1244',
             'CM241':'1411'}  
    instructors = {'CS101':'Haynes',
                   'CS102':'Alvarado',
                   'CS103':'Rich',
                   'NT110':'Burke',
                   'CM241':'Lee'} 
    times =  {'CS101':'8:00 am',
              'CS102':'9:00 am',
              'CS103':'10:00 am',
              'NT110':'11:00 am',
              'CM241':'1:00 pm'}

    # Student name is first line of output
    print('Sarah Vigstol\n')
    # Call welcome function
    welcome()
    
    # Prompt user for a course number
    course = input('Please enter a course number: ').upper()

    # Check dictionaries for entered course
    if course in rooms:
        if course in instructors:
            if course in times:
                # Display course information if found
                print(f'Here are the details for {course}:')
                print(f'\t* Room: {rooms[course]}')
                print(f'\t* Instructor: {instructors[course]}')
                print(f'\t* Time: {times[course]}')
    else:
        # Display message if course not found
        print('Course not found.')

# Define welcome message function
def welcome():
    print('Course Detail Lookup')
    print('--------------------')

# Call the main function
main()


# Program output
'''
Sarah Vigstol

Course Detail Lookup
--------------------
Please enter a course number: CS101
Here are the details for CS101:
	* Room: 3004
	* Instructor: Haynes
	* Time: 8:00 am
>>> 
'''
