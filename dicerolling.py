import math
import random
import time

dice = random.randint(1,6)
computerDice = random.randint(1,6)


def rolldice(roll):
    print("Dice 1 is rolling...")
    time.sleep(1)
    print("You rolled: ", + dice)
    print("-------------------")
    
def computerRoll(computerRoll):
    print("Computer Dice is rolling...")
    time.sleep(1)
    print("Computer rolled: ", +computerDice)
    
    
        
rolldice(dice)
computerRoll(computerRoll)
print("\n")

if dice > computerDice:
    print("You won!")
elif computerDice > dice:
    print("Computer Won!")
print("\n")
