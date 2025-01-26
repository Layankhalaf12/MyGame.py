#Write a  program in python to simulate a game called MyGame.py.
#  In this game you will use three variables called player1, player2 and player3. Each player rolls a dice, 
# which means that the variables are initialized with random integers ranging from 1 to 6. Compare the values of player1, 
# player2 and player3 to find the highest value. Print that highest value. Use comments and import statements wherever applicable. 
# Give screenshots of the code, output and git repository containing this program.

import random
import math
player1=0
player2=0
player3=0
winner=0
for winner in range (1,7):
  player1=int(input("please Enter player1"))
  player2=int(input("Enter the player2 :"))
  player3=int(input("Enter the player3 :"))
  print(winner)
  largest=0
  largest=max(player1,player2,player3 )
  print("the largest number between the three players is "+str(largest))
   
     
