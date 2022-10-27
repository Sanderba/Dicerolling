import math
import random
import time
import colorama


dice = random.randint(1,6)
computerDice = random.randint(1,6)


def rolldice(roll, color=colorama.Fore.YELLOW):
    print(color+"You are rolling...")
    time.sleep(1)
    print("You rolled: ", + dice)
    print("-------------------")
    
def computerRoll(computerRoll, color=colorama.Fore.CYAN):
    print(color +"Computer rolled: ", +computerDice)
    print("Computer Dice is rolling...")
    time.sleep(1)
    

rolldice(dice)
computerRoll(computerRoll)
print(colorama.Fore.RESET)        
print("\n")

if dice > computerDice:
    print(colorama.Fore.GREEN + "You won!")
elif computerDice > dice:
    print(colorama.Fore.RED + "Computer Won!")
elif dice == computerDice:
    print("Draw!")    

print(colorama.Fore.RESET)   