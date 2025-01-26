#Implement the following as version2 of problem 1 given in this document. Suppose all players in problem1 roll the dice two times. 
#  The score of each player is the sum of the previous and current value on the dice. The program should print the highest score.
#  Use comments and import statements wherever applicable. Provide screenshots of the code,  
# output and git repository

import random
from MyGame import player1 #import player 1,2,3 values from MyGame.py
from MyGame import player2
from MyGame import player3
player1A= random.randint(1,6)
if __name__ == "__main__": #use it to block the input while importing other file 
   print("player 1 second time is "+str(player1A))

player2A=random.randint(1,6) #ask find a random number between 1-6
if __name__ == "__main__":
   print("player 2 second time is "+str(player2A)) # print the value of player2A round 2

player3A=random.randint(1,6)
if __name__ == "__main__":
 print("player 3 second time is "+str(player3A))
 
winner1=player1+player1A
if __name__ == "__main__":
     print("the sum of player2 is "+ str(winner1))

winner2=player2+player2A
if __name__ == "__main__":     
   print("the sum of player2 is "+ str(winner2))

winner3=player3+player3A
if __name__ == "__main__":      
     print("the sum of player3 is "+ str(winner3))

if __name__ == "__main__": # use if statement to find the highest value by comparing the sum of the 3 players.
  if (winner1>winner2 and winner1>winner3) :
    print("the highest score is "+ str(winner1))
  if (winner2>winner1 and winner2>winner3) :
     print("the highest score is "+ str(winner2))
  if(winner3>winner1 and winner3>winner1): 
     print("the highest score is "+ str(winner3)) 
