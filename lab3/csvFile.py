# CSV File Handling
# ● Read data from a CSV file containing student records (roll number, name, marks)
# ● Display all student records
# ● Handle file-related and data conversion errors using try-except
import csv

try:
    file = open("students.csv", "r")
    reader = csv.reader(file)

    print("Student Records:")
    print("Roll No\tName\tMarks")

    for row in reader:
        try:
            roll = int(row[0])
            name = row[1]
            marks = float(row[2])
            print(f"{roll}\t{name}\t{marks}")
        except (ValueError, IndexError):
            continue

    file.close()

except FileNotFoundError:
    print("Error: CSV file not found")
except Exception as e:
    print("Unexpected error:", e)
