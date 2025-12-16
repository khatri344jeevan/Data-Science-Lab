# 3. Student Marks Manager 
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute 
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks. 
def find_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "D"

students = {
    "Ram": [80, 75, 88],
    "Sita": [65, 70, 60],
    "Hari": [90, 85, 92],
    "Gita": [40, 55, 50]
}