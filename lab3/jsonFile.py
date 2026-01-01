# 4. Writing and Reading JSON Data
# ● Stores student details (ID, name, and marks) in a JSON file
# ● Reads the JSON file and displays the student information
# ● Handles exceptions related to file access and JSON decoding
import json

try:
    student = {
        "id": 101,
        "name": "Ram",
        "marks": 88
    }

    file = open("student.json", "w")
    json.dump(student, file)
    file.close()

except Exception as e:
    print("Error while writing to JSON file:", e)


try:
    file = open("student.json", "r")
    data = json.load(file)
    file.close()

    print("Student Details:")
    print("ID:", data["id"])
    print("Name:", data["name"])
    print("Marks:", data["marks"])

except FileNotFoundError:
    print("Error: JSON file not found")
except json.JSONDecodeError:
    print("Error: Invalid JSON format")
except Exception as e:
    print("Unexpected error:", e)
