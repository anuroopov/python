#BMI Calculator

height=input("Enter your height in m :")
weight=input("Enter your weight in kg:")
bmi=float(weight)/float(height) ** 2
#using fstring
print (f"Your BMI is: {bmi} ")
if bmi<=18.5:
    print("You are Under Weight ! ")
else:
    if bmi <= 25:
       print(" You have a Normal weight !")
    elif bmi <= 30:
       print(" You are Over weight !")
    elif bmi <= 35:
       print(" You are Obese !!")
    else:
        print(" You are Clinically Obese !!")
