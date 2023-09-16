import random
names= input("Pls enter the names of peoples participating separated by commas:")
print(names)
names_list=names.split(",")
print(names_list)
print(f"{names_list[random.randint(0, 7)]} will pay the bill")

-------------------------------

import random
names= input("Pls enter the names of peoples participating separated by commas:")
print(names)
names_list=names.split(",")
print(names_list)

count=len(names_list)
print(f"{names_list[random.randint(0, count)]} will pay the bill")
----------------------------------