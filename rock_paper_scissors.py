import random
#rock , scissors = 02
#scissors, paper = 21
#paper, rock     = 10
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#------------- user input -----------------------#
user_input = int(input("Enter users choice: [Rock = 0 | Scissors = 2 | Paper = 1]:")) # Enter 0, 1 , 2
print("Pls enter user input :",user_input) 
if user_input == 1: 
 print (paper)
if user_input == 2:
  print (scissors)
if user_input == 0:
  print (rock)
#------------- Computer input -----------------------#
computer_choice = random.randint(0,2)
print("computer\'s choice:",computer_choice)

if computer_choice == 1: 
 print (paper)
if computer_choice == 2:
  print (scissors)
if computer_choice == 0:
  print (rock)
#---------------- Who Wins ---------------------------#
print("selections:",str(user_input) + str(computer_choice))
selections=str(user_input) + str(computer_choice)
if selections[0] == '0' and selections[1] == '2':
   print ("user Wins")
elif  selections[0] == '1' and selections[1] == '0':
   print ("user Wins")   
elif  selections[0] == '2' and selections[1] == '1':
   print ("user Wins")   
else:
    if selections[0] == selections[1]:
      print ("DRAW")
    #elif  selections[0] == '1' and selections[1] == '1':
      #print ("DRAW")   
    #elif  selections[0] == '2' and selections[1] == '2':
     # print ("DRAW") 
    else:
      print ("user Lost- better luck next tme ")   