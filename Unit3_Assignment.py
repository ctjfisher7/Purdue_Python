''' Connor Fisher IT244 Python Programming
	Unit 2 Assignment Created 20220221
'''
#Program to caculate the average grade for a student.
#This section contains the variables/input.
numOfGrades = int(input('\nEnter the number of grades to process: '))
studentName = input ('\nEnter the students name: ')
count = 0
stuAvg = 0

#While loop that takes in all the grades.
while count < numOfGrades:
    assignGrade = int(input('\nEnter the assignment grade: '))
    stuAvg = stuAvg + assignGrade
    count = count + 1

#Calcuating the average for a new value to stuAvg
stuAvg = stuAvg/numOfGrades

#Print statement with the information that needed to be given.
#Thought of a few ways to conducted the print statement but this one worked the best.
#Can't use + in a print statement with two variable and text, it tries to add them with the string text.
#Added the .title to make sure the name becomes capitalized for the print statement.
print('\n\n',studentName.title(),'has an average of:', stuAvg)
