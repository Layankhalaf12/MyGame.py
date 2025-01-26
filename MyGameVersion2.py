#Implement the following as version2 of problem 1 given in this document. Suppose all players in problem1 roll the dice two times. 
#  The score of each player is the sum of the previous and current value on the dice. The program should print the highest score.
#  Use comments and import statements wherever applicable. Provide screenshots of the code,  
# output and git repository
import random
import math
player1=0
player2=0
player3=0
winner=0
winner2=0
winner3=0
for winner in range (1,7):
  player1=int(input("please Enter player1"))
  player1A= int(input("please Enter player1A"))
  winner= player1+player1A
  print(winner)

  for winner2 in range(1,7):
    player2=int(input("Enter the player2 :")) 
    player2A=int(input("Enter the player2A :"))
    winner2=player2+player2A
    print(winner2)

for winner3 in range(1,7):
  player3=int(input("Enter the player3 :"))
  player3A=int(input("Enter the player3A :"))
  winner3=player3+player3A
  print(winner3)
