# Define a function that takes two numbers as arguments, and returns their greatest
# common divisor (GCD).
def gcd(a, b):
    gcd=1
    for i in range(1, min(a, b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"The GCD of {a} and {b} is {gcd(a, b)}")