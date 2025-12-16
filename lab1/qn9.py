# Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and
# Kelvin, based on the choice of user
celsius=float(input("Enter temperature in Celsius: "))
print("Choose the conversion option:")
print("1. Fahrenheit")
print("2. Kelvin")
choice=int(input("Enter your choice (1 or 2): "))
if choice==1:
    fahrenheit=(celsius*9/5)+32
    print(f"Temperature in Fahrenheit: {fahrenheit}")
elif choice==2:
    kelvin=celsius+273.15
    print(f"Temperature in Kelvin: {kelvin}")
else:
    print("Invalid choice! Please select 1 or 2.")