import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []
hitorstand = 'y'
while hitorstand == 'y':
    if len(player) == 2 and len(computer) == 2 :
        player = [cards[random.randint(0, 12)]] + player
        print(f"Your final hand {player} current score : {sum(player)}")

        if sum(computer) <= 17 :
            computer = [cards[random.randint(0, 12)]] + computer
            print(f"Computers final hand {computer}, current score : {sum(computer)}")
        else:
            print(f"Computers final hand {computer}, current score : {sum(computer)}")
            if sum(player) >= sum(computer) and sum(player) <= 21 :
                  print("you win")
            else:
                  print("Computer win")
    else:
       # print(cards[random.randint(0,13)],cards[random.randint(0,13)])
        player = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
        print(f"Your cards {player}, current score : {sum(player)}")

        computer = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
        print(f"Computers first cards  {computer[0]} ")

        hitorstand = input("Type 'y' to get another card, type 'n' to pass: ")
