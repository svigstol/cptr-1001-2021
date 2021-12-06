# Ch4Ex4.py
# Ch4Ex4
# Sarah Vigstol
# This program prompts the user for the speed of a vehicle in miles per
# hour and the number of hours traveled, validates both inputs, then
# calculates and displays the distance the vehicle has traveled for each
# hour of that time period.

# Student name must be the first line of output
print('Sarah Vigstol')

# Display welcome message
print('Distance Traveled Calculator')

# Prompt user for vehicle speed and assign the value to new variable
speed = int(input('What is the speed of the vehicle in miles per hour? '))
# Validate user input
while speed < 0 or speed > 120:
    print(f'You entered: {speed}mph')
    print('Speed cannot be negative nor exceed 120mph. Try again.\n')
    speed = int(input('What is the speed of the vehicle in miles per hour? '))
    
# Prompt user for hours traveled and assign the value to new variable
time = int(input('How many hours has it traveled? '))
# Validate user input
while time < 0 or time > 9:
    print(f'You entered: {time} hours')
    print('Time cannot be negative nor exceed 9 hours. Try again.\n')
    time = int(input('How many hours has it traveled? '))
    
# Calculate total distance traveled and assign to new variable
distance = speed * time

# Calculate and display distance traveled for each hour of the given time
print('Hour\tDistance Traveled')
print('-------------------------')
for  hour in range(time): # Range function uses 'time' to create iterable
    hour += 1
    distPerHour = (distance / time) * hour
    print(f'{hour}\t{distPerHour:.0f}')

# Program output
'''
Sarah Vigstol
Distance Traveled Calculator
What is the speed of the vehicle in miles per hour? -55
You entered: -55mph
Speed cannot be negative nor exceed 120mph. Try again.

What is the speed of the vehicle in miles per hour? 55
How many hours has it traveled? -5
You entered: -5 hours
Time cannot be negative nor exceed 9 hours. Try again.

How many hours has it traveled? 5
Hour	Distance Traveled
-------------------------
1	55
2	110
3	165
4	220
5	275
>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/Ch4Ex4.py
Sarah Vigstol
Distance Traveled Calculator
What is the speed of the vehicle in miles per hour? 150
You entered: 150mph
Speed cannot be negative nor exceed 120mph. Try again.

What is the speed of the vehicle in miles per hour? 120
How many hours has it traveled? 12
You entered: 12 hours
Time cannot be negative nor exceed 9 hours. Try again.

How many hours has it traveled? 9
Hour	Distance Traveled
-------------------------
1	120
2	240
3	360
4	480
5	600
6	720
7	840
8	960
9	1080
>>> 
= RESTART: /media/svigstol/files/My Docs/School/Course Resources/Fall 2021/Intro to Prog/Ch4Ex4.py
Sarah Vigstol
Distance Traveled Calculator
What is the speed of the vehicle in miles per hour? 78
How many hours has it traveled? 9
Hour	Distance Traveled
-------------------------
1	78
2	156
3	234
4	312
5	390
6	468
7	546
8	624
9	702
>>> 
'''
