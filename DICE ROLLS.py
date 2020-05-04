""" HAROLD BERNIE P. GARCIA / Antonio Riotoc
   DATALOG  LP1.3
   APRIL 23, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""
import random

print("[1] [2] [3] [4] [5] [6]")
print("_____________________________")


print("Player 1")
player1a = int(input("Enter dice number:"))             # PLAYERS INPUTS THERE DICE of CHOOSE
player1b = int(input("Enter dice number:"))              # PLAYERS INPUTS THERE DICE of CHOOSE
print("player choosen no:", player1a , " & " , player1b)      # prints DICE
print("_____________________________")



print("CPU:")
from random import randint                                    #
for _ in range(1):                                            # CPU generate 1 random dice
	value1 = randint(1, 6)                                    # Random number Range dice ([1] [2] [3] [4] [5] [6])
cpu1 = value1                                                 # outputs Random number

for _ in range(1):                                            # CPU generate 1 random dice
	value2 = randint(1, 6)                                    #  Random number Range dice ([1] [2] [3] [4] [5] [6])
cpu2 = value2                                                 # outputs Random number

print("player choosen no:", cpu1 , " & " , cpu2)              # prints Random value

print("_____________________________")

print("Dice: [6] [1] [4]  [2] [5] [1] [3] [4] [5] [2] [6] [3]")         #
print()
print ("Rolling the dices....")                               # Rolling Dice Process


for _ in range(1):
	    DICE1 = randint(1, 6)                                 # 1st dice ROll
D1= DICE1

for _ in range(1):                                            # 2nd Dice roll
		DICE2 = randint(1, 6)
D2 = DICE2


print(".[",D2,"]..[",D1,"].")                                 # prints DICE

print()
print("________________________")
x = player1a + player1b                                       # ADDs DICE player 1
z = cpu1 + cpu2                                               # ADDs DICE Cpu

a = D1  + D2                                                  # ADDS TOTAL ROLLED DICE
print("total sum of dice:", a)


print("player1:", x)
print("CPU:", z)

if x >= a:                                                    # this FOrmula Tells the Winner
    print("That Player WINS" , "\***\**/***/")
else:
    print("That CPU WINS" , "\***\**/***/")