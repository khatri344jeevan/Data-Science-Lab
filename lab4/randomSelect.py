# 4. Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection.
import random
# students=["Ram","Ram","Ram","Ram","Ram","Ram"]
students=[]
for i in range(6):
    name=input(f"Enter the name of student{i+1}:")
    students.append(name)

volunteers=random.sample(students,3)
print("Volunteers:",volunteers)