import bmi

def army_eligibility(age,bmi):
    if 18 <= age <= 40 and 18.5 <= bmi <= 29.9:
        print("Eligible for army entrance")
    else:
        print("Not eligible for army entrance")

age = int(input("Enter your age:"))
# height = float(input("Enter your height in meters:"))
# weight = float(input("Enter your weight in kg:"))
height_unit=input("Height unit (cm/feet/inches):")
weight_unit=input("Weight unit (kg/pounds):")
height=float(input("Enter height:"))
weight=float(input("Enter weight:"))



armybmi = bmi.bmi_calculator(height,weight,height_unit,weight_unit)
print("Your BMI is:",armybmi)
army_eligibility(age,armybmi)