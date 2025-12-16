# Write a program that takes a list of numbers as input, and returns the largest number in
# the list.
def largest(numbers):
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print(f"the largest is{largest}")
numbers=[]

n = int(input("Enter the no. of items(of numbers) want to add in list: "))

for i in range(n):
    number=int(input(f"Enter:"))
    numbers.append(number)
largest(numbers)
print(numbers)