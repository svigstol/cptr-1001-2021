# Ch5Ex16.py
# Ch5Ex16
# Sarah Vigstol
# This program generates 100 random numbers (10 per line) and determines how
# many are even and how many are odd.

# Import random module to generate random numbers
import random

# Student name must be the first line of output
print('Sarah Vigstol')     

# Define function that determines whether a number is even or odd
def isEven(number):
    if (number % 2) == 0:
        # Set status to true if number is even
        status = True
    else:
        # Set status to false if number is odd
        status = False
    # Return value of status variable to the program
    return status

# Define function that tracks total number of odd and even numbers, then
# returns both totals to the program
def numberCounter():
    # Initialize accumulators to track odd and even numbers
    even = 0
    odd = 0
    # Initialize accumulator to track number of times loop has repeated
    counter = 0
    while counter < 100:
        # Generate random number
        number = random.randint(1, 999)
        # Call isEven function to determine whether even or odd and assign
        # result to new local variable
        status = isEven(number)

        if status == True:
            # If even, increase even counter by 1
            even += 1
        else:
            # If odd, increase odd counter by 1
            odd += 1
        # Increase counter by 1 for each loop iteration
        counter += 1
        
        # Display number
        # Create a new line every 10 iterations
        if counter % 10 == 0:
            print(number, '\n')
        else:
            print(number, end=' ')
    # Return totals
    return even,odd

# Call numberCounter function and assign returned results to new variables
even,odd = numberCounter()

# Display number of even and odd numbers
print(f'Out of 100 random numbers, {odd} were odd and {even} were even.')


# Program output
'''
Sarah Vigstol
642 716 182 501 564 202 129 458 834 697 

12 833 430 629 655 96 340 385 109 965 

458 987 761 319 309 513 629 208 507 123 

674 658 728 1 623 285 342 993 717 635 

891 715 458 101 718 809 347 556 454 277 

648 553 147 128 874 219 968 932 994 901 

212 688 204 51 334 27 129 635 691 25 

24 476 887 809 273 42 388 732 673 154 

860 207 266 324 487 567 625 906 9 869 

163 556 510 72 309 646 960 246 785 221 

Out of 100 random numbers, 53 were odd and 47 were even.
>>> 
'''
