a = input("Enter the first number: ")
b = input("Enter the second number: ")

if '.' in a:
    a = float(a)
else:
    a = int(a)
if '.' in b:
    b = float(b)
else:
    b = int(b)
sum = a + b
print("The sum is", sum)