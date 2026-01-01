# File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers

try:
    file = open("numbers.txt", "r")
    total = 0
    count = 0

    for line in file:
        try:
            num = float(line.strip())
            total += num
            count += 1
        except ValueError:
            continue

    file.close()

    if count > 0:
        average = total / count
        print("Sum:", total)
        print("Average:", average)
    else:
        print("No valid numbers found")

except FileNotFoundError:
    print("Error: File does not exist")
except Exception as e:
    print("Unexpected error:", e)
