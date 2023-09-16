# This is a sample Python script.
print("Hello World")

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])
# print(len(street_name))

# num_char = len(input("What is ur name?:"))
# new_num_char = str(num_char)   #type casting str/ int /float
# print("Your name has " + new_num_char + "characters")

#Sum of digits
#--------------------
# number=input("Enter a two digit number:")
# print(type(number))
# #print(number)
# sumofdigits= int(number[0]) + int(number[1])
# print(sumofdigits)

# PEMDASLR - precednce order ( left to right )
# ()
# **
# * /
# + -
#print(3 * 3 + 3/3 -3)  = 7
#print(3 * (3 + 3/3 -3)) = 3

#BMI Calculator
# height=input("Enter your height in m :")
# weight=input("Enter your weight in kg:")
# bmi=float(weight)/float(height) ** 2
# #using fstring
# print (f"Your BMI is: {bmi} ")
# if bmi<=18.5:
#     print("You are Under Weight ! ")
# else:
#     if bmi <= 25:
#        print(" You have a Normal weight !")
#     elif bmi <= 30:
#        print(" You are Over weight !")
#     elif bmi <= 35:
#        print(" You are Obese !!")
#     else:
#         print(" You are Clinically Obese !!")


#life in weeks challenge

# age=int(input("What is your current age ?"))
# yrsleftto90 = 90 - age
# print(f"years to 90 : {yrsleftto90}")
# days = int(yrsleftto90) * 365
# #print (f"Days: {days}")
# weeks = round(float(days/7))
# #print (f"Weeks: {weeks}")
# months = round(weeks/4)
# #print (f"Months: {months}")
#
# print(f"You have {days} days, {weeks} weeks, and {months} months more - Enjoy ur ife")
#

#Day 3 -conditional Logic

#Even or odd

# number=int(input("Enter the number: "))
# check=number%2
# print(check)
# if check == 0:
#     print("This is a Even number!!")
# else:
#     print("This is a Odd number!!")


#leap year list
# 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840,
# 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880,
# 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928,
# 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
# 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020

#leap year

year=int(input("Enter the year:"))
if year%4 == 0:
   if year%100 == 0:
       if year % 400 == 0:
           print ("leap year")
       else:
           print("Not a leap year")
   else:
    print ("Leap year")
else:
    print(" Not Leap Year!!")


