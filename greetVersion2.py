4.	User inputs and concatenation
Write a program called greet.py  that asks the user to type their name and store it in a variable called name. 
The program should print a greeting for the user. For example if the user’s name is Joe, the program should print “ Good Morning Joe”. 
Use comments wherever applicable. Explain your logic. Create a version2 of this problem in your git repository. 
In version2 you should print the message three times. Give screenshots of the code, outputs and the git repository
import greet
from greet import name #import greet file so we dont add more codes about asking the user to enter name 
for name in range(3): # asking the program to print the message 3 times
  print("good morning"+str(name))
  
