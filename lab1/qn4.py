# Write a python program that prints the Fibonacci series up to n terms.
n=int(input("Enter number of terms"))
a=0
b=1
for i in range(n):
    print(a)
    temp=a+b
    a=b
    b=temp