# Ch5Ex15.py
# Ch5Ex15
# Sarah Vigstol
# This program prompts the user for five test scores, then displays a letter
# grade for each score and the average test score.

# Student name must be the first line of output
print('Sarah Vigstol')

# The welcome function displays a welcome message to the user
def welcome():
    print('Welcome to the Test Average and Grade Calculator\n')

# Define function that accepts five scores as arguments, then returns the
# average of the scores
def calcAverage(score1, score2, score3, score4, score5):
    # Declare constant for number of test scores accepted as input
    NUM_SCORES = 5
    average = (score1 + score2 + score3 + score4 + score5) / NUM_SCORES
    return average

# Define fuction that returns a letter grade based on each score's
# numerical value
def determineGrade(score):
    if score >= 90:
        grade = 'A'
        return grade
    elif score > 79 and score < 90:
        grade = 'B'
        return grade
    elif score > 69 and score < 80:
        grade = 'C'
        return grade
    elif score > 59 and score < 70:
        grade = 'D'
        return grade
    else:
        grade = 'F'
        return grade

# Call welcome function to display welcome message
welcome()
# Get five scores from user
# Call the determineGrade function for each score to get the appropriate
# letter grade and assign to a new variable each time
score1 = int(input('Enter the first score. '))
grade1 = determineGrade(score=score1)

score2 = int(input('Enter the second score. '))
grade2 = determineGrade(score=score2)

score3 = int(input('Enter the third score. '))
grade3 = determineGrade(score=score3)

score4 = int(input('Enter the fourth score. '))
grade4 = determineGrade(score=score4)

score5 = int(input('Enter the fifth score. '))
grade5 = determineGrade(score=score5)

# Call calcAverage function to calculate the average score and assign
# the value to a new variable
averageScore = calcAverage(score1, score2, score3, score4, score5)

# Call determineGrade function, passing averageScore as an argument to
# determine the average letter grade, then assign result to new variable
averageGrade = determineGrade(averageScore)

# Define function that prints all scores, corresponding letter grades, and
# the average test score in a report form
def testScores():
    print(f'''
score\t\tnumeric grade\tletter grade
-----------------------------------------------------------
score 1:\t{score1}\t\t{grade1}
score 2:\t{score2}\t\t{grade2}
score 3:\t{score3}\t\t{grade3}
score 4:\t{score4}\t\t{grade4}
score 5:\t{score5}\t\t{grade5}
------------------------------------------------------------
Average score:\t{averageScore}\t\t{averageGrade}
''')

# Call testScores function to display score report
testScores()

# Program output
'''
Sarah Vigstol
Welcome to the Test Average and Grade Calculator

Enter the first score. 84
Enter the second score. 93
Enter the third score. 97
Enter the fourth score. 88
Enter the fifth score. 79

score		numeric grade	letter grade
-----------------------------------------------------------
score 1:	84		B
score 2:	93		A
score 3:	97		A
score 4:	88		B
score 5:	79		C
------------------------------------------------------------
Average score:	88.2		B

>>> 
'''
