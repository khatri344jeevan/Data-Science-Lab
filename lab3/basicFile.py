# 1. Basic File Read & Write
# ● Create a text file and write multiple lines into it
# ● Read the contents of the file and display them on the screen
# ● Handle the case where the file does not exist using try-except
# Writing multiple lines to a file
try:
    file = open("sample.txt", "w")
    file.write("Python File Handling")
    file.write("Reading and Writing Files")
    file.write("Exception Handling Example")
    file.close()
except Exception as e:
    print("Error while writing to file:", e)

try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File Contents:")
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File does not exist")
except Exception as e:
    print("Unexpected error:", e)
