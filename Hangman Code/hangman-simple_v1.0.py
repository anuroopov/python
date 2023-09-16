import random
word_list = ['ardvark','baboon','camel']
word_picked = random.choice(word_list)
print ( word_picked)
blank_list = []
for i in range(0,len(word_picked)):
    blank_list.append("_")
print(blank_list) 

user_trys=0
while user_trys <=5:
    if '_' in blank_list:
        print("user_trys",user_trys)
        user_guess_letter = input("Enter the User guess letter: ").lower()
        #res=[]
        for i in range(0, len(word_picked)):
            if word_picked[i] == user_guess_letter:
                blank_list[i] = user_guess_letter    
          
        #for i in range(0, len(word_picked)):
         #print (i)
         #   if word_picked[i] == user_guess_letter:
              #  res.append(i) 
               #break
        #print ("res:" , res)
        #for i in res:
        #    blank_list[i] = user_guess_letter
        
        print (blank_list)
        user_trys=user_trys+1   
    else:
        user_trys=user_trys+1
        print ( "******************* You Won  ***********************")
    if user_trys >=6 and '_' in blank_list:
        print ( "******************* You Failed *********************")