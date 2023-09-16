import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['ardvark','baboon','camel']
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
        print("user_trys",var_lives)
        user_guess_letter = input("Enter the User guess letter: ").lower()
        res=[]
        for i in range(0, len(word_picked)):
        
            if word_picked[i] == user_guess_letter:
                blank_list[i] = user_guess_letter  
        if  user_guess_letter  not in  word_picked:
            var_lives= var_lives -1
        
        print(stages[var_lives])
        
        print (blank_list)
        #user_trys=user_trys+1   
        print(var_lives)
    else:
        var_lives= 0
        print(var_lives)
        print ( "******************* You Won  ***********************")
    if var_lives <=0 and '_' in blank_list:
        print(var_lives)
        print ( "******************* You Failed *********************")