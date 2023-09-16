import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)

word_picked = random.choice(word_list)
print ( word_picked)
blank_list = []
for i in range(0,len(word_picked)):
    blank_list.append("_")
print(blank_list) 

user_trys=0
var_lives=6
while var_lives != 0:
    if '_' in blank_list:
        user_guess_letter = input("Enter the User guess letter: ").lower()
        for i in range(0, len(word_picked)):
            if word_picked[i] == user_guess_letter:
                blank_list[i] = user_guess_letter  
        if  user_guess_letter  not in  word_picked:
            print("Letter is not used & u lost one life .... !!")
            var_lives= var_lives -1
        
        print(stages[var_lives])
        print (blank_list)
    else:
        var_lives= 0
        print ( "******************* You Won  ***********************")
    if var_lives <=0 and '_' in blank_list:
        print ( "******************* You Failed *********************")