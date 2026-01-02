import random
PC = random.randint(1,5)
           
player = int(input("choose a random number from 1 to 5"))

if PC == player:
    print("you win")

elif PC > player or PC < player:
    print("you lose")

else:
    print("choose 1-5")
