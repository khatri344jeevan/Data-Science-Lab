def bmi_calculator(height, weight, height_unit="cm", weight_unit="kg"):

    if height_unit.lower() in ["feet", "ft"]:
        height = height * 0.3048
    elif height_unit.lower() in ["inches", "inch", "in"]:
        height = height * 0.0254
    elif height_unit.lower() in ["cm"]:
        height = height / 100
    else:
        print("INvalid height unit")
        exit()
        
    if weight_unit.lower() in ["pounds", "lb", "lbs"]:
        weight = weight * 0.453592
    elif weight_unit.lower() in ["kg"]:
        weight=weight
    else:
        print("Invalid weight unit")
        exit()

    bmi = weight / (height ** 2)
    # print("BMI:", round(bmi, 2))
    return bmi

def category(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    print("Category:", category)


def display():
    height=float(input("Enter height:"))
    weight=float(input("Enter weight:"))
    height_unit=input("Height unit (cm/feet/inches):")
    weight_unit=input("Weight unit (kg/pounds):")
    bmi=bmi_calculator(height,weight,height_unit,weight_unit)
    print(bmi)
    category(bmi)

# display()