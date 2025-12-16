# 10. Write multiple python files with separate functions for the following cases: 
# a. A program that takes the age of an user, and gives their birth year, and if birth 
# year was a leap year. 
# b. A program that computes the Body Mass Index (BMI) of a user, taking their 
# height and weight as input. The program should allow the user to enter their 
# height in either feet/inches or centimeters and their weight in either kilograms or 
# pounds. 
# Extend the program to convert BMI into a category based on standard criteria: 
# ■ Underweight: < 18.5 
# ■ Normal weight: 18.5 - 24.9 
# ■ Overweight: 25 - 29.9 
# ■ Obese: ≥ 30
# c. A program that checks if a user is eligible for army entrance based on their BMI 
# and age. The eligibility criteria are as follows: 
# ■ Age must be between 18 and 40 years. 
# ■ BMI must be within the range of 18.5 to 29.9.

def birth_year_and_leap(age):
    from datetime import datetime
    current_year=datetime.now().year
    year_of_birth=current_year-age
    print("Year of Birth:",year_of_birth)
    if (year_of_birth%4==0 and year_of_birth%100 != 0) or (year_of_birth%400==0):
        print("Birth year was a leap year")
    else:
        print("Birth year was not a leap year")

age=int(input("Enter your age:"))
birth_year_and_leap(age)
