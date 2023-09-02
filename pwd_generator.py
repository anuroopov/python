# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_letters = random.choices(letters, k=no_letters)
print("pwd_letters:", pwd_letters)
pwd_numbers = random.choices(numbers, k=nr_numbers)
print("pwd_numbers:", pwd_numbers)
pwd_sysmbols = random.choices(symbols, k=nr_symbols)
print("pwd_letters:", pwd_sysmbols)

pwd_merged = pwd_letters + pwd_numbers + pwd_sysmbols

random.shuffle(pwd_merged)
print("pwd_merged:", pwd_merged)
x=""
for i in pwd_merged:
  #print (i)
  x=x+i
print("Password generated is :", x)
#------------------------------------------------------------
#Eazy Level( Angelina ) 
 
# password = ""
#
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
#
#for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
#
# print(password)
#
##----------------------------------------------------------------
##Hard Level
#password_list = []
#
#for char in range(1, nr_letters + 1):
#  password_list.append(random.choice(letters))
#
#for char in range(1, nr_symbols + 1):
#  password_list += random.choice(symbols)
#
#for char in range(1, nr_numbers + 1):
#  password_list += random.choice(numbers)
#
#print(password_list)
#random.shuffle(password_list)
#print(password_list)
#
#password = ""
#for char in password_list:
#  password += char
#
#print(f"Your password is: {password}")
