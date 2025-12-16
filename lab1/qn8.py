# Write a program that checks if a year is a leap year.
year=int(input("ENter year"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("This is leap year")
else:
    print("This is not leap year")