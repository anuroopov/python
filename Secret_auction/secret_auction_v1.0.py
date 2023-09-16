
#Secret auction using Dictionary
# Clear usage in ipython & windows

import os

#from IPython.display import clear_output
print(logo)
print("Welcome to the secret auction program.")
print("Please START your bid :")

dict_bid={}
continue_bid="yes"
while continue_bid == "yes":
    var_name=input("What's your name ?:")
    var_bid=int(input("What's your bid ?: $"))
    dict_bid[var_name] = var_bid    
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.")

    #if continue_bid == "yes":
    #clear_output()    # ipython way
    os.system('cls')
#print("dict_bid",dict_bid) 

#Deciding the winner    
highest_bid = 0
high_key = ""
for key in dict_bid:
    if dict_bid[key] > highest_bid:
        highest_bid = dict_bid[key]
        high_key = key              
               
print(f"The winner is {high_key} with a bid of ${highest_bid}")
