# 5. Menu-Driven File Operations
# ● Write data to a file
# ● Read data from a file
# ● Append data to a file
# ● Handle invalid user input and file errors using exception handling
def write_file(filename):
    try:
        data = input("Enter data to write to the file: ")
        with open(filename, "w") as file:
            file.write(data + "\n")
        print("Data written successfully.")
    except Exception as e:
        print("Error writing to file:", e)

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        print("File Contents:\n", content)
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print("Unexpected error:", e)

def append_file(filename):
    try:
        data = input("Enter data to append: ")
        with open(filename, "a") as file:
            file.write(data + "\n")
        print("Data appended successfully.")
    except Exception as e:
        print("Error appending to file:", e)

filename = "data.txt"

while True:
    print("\nMenu:")
    print("1. Write to File")
    print("2. Read from File")
    print("3. Append to File")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        write_file(filename)
    elif choice == 2:
        read_file(filename)
    elif choice == 3:
        append_file(filename)
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
