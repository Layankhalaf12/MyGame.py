#Write a  program in python to simulate a game called MyGame.py.
#  In this game you will use three variables called player1, player2 and player3. Each player rolls a dice, 
# which means that the variables are initialized with random integers ranging from 1 to 6. Compare the values of player1, 
# player2 and player3 to find the highest value. Print that highest value. Use comments and import statements wherever applicable. 
# Give screenshots of the code, output and git repository containing this program.

import random



player1 = random.randint(1, 6)  # Player 1 rolls the dice
player2 = random.randint(1, 6)  # Player 2 rolls the dice
player3 = random.randint(1, 6)  # Player 3 rolls the dice
if __name__ == "__main__":
 print("player 1 is "+str(player1))
 print("player 2 is "+str(player2))
 print("player 3 is "+str(player3))
if __name__ == "__main__": # this code will run only when direct executed not when import
 largest=max(player1,player2,player3 )
 print("the largest number between the three players is "+str(largest))
