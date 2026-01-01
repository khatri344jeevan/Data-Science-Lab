# 3. Student Marks Manager 
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute 
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks. 
# def find_grade(average):
#     if average >= 80:
#         return "A"
#     elif average >= 60:
#         return "B"
#     elif average >= 40:
#         return "C"
#     else:
#         return "D"

# students = {
#     "Ram": [80, 75, 88],
#     "Sita": [65, 70, 60],
#     "Hari": [90, 85, 92],
#     "Gita": [40, 55, 50]
# }
students={}
n =int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter student name: ")
    marks_input=input("Enter marks separated by space: ")
    marks=[]

    for m in marks_input.split():
        marks.append(int(m))

    students[name] = marks

student_data = {}
for name in students:
    marks = students[name]
    average = sum(marks)/len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"

    student_data[name] = (marks,average,grade)

    print(name, "Marks:", marks,"Average:", round(average, 2),"Grade:", grade)


avg_list = []

for name in student_data:
    avg_list.append((student_data[name][1], name))

avg_list.sort(reverse=True)

print("Top 2 students based on average marks:")

for i in range(2):
    average =avg_list[i][0]
    name=avg_list[i][1]
    grade=student_data[name][2]

    print("name:", name, "average:", round(average, 2), "grade:", grade)