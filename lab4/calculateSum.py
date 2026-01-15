# Given a list of student names and a list of their corresponding scores, use the zip()
# function to pair them together and then apply the reduce() function from the
# functools module to calculate the total sum of all scores.
from functools import reduce
students = []
scores = []
n = int(input("Enter number of students:"))
for i in range(n):
    name = input(f"Enter the name of student:")
    students.append(name)
    score = int(input(f"Enter the score of student:"))
    scores.append(score)

zipped=zip(students,scores)
print("Zipped",list(zipped))

total_score=reduce(lambda x,y:x+y,scores)


print("Total sum of all scores:",total_score)