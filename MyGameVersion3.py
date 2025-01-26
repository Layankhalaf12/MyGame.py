#3.	Program logic and Arithmetic Operators
#Implement the following as version 3 and add the code to computer average score of all three players in problem 2.  
# The average will be calculated and printed twice. Once using ‘/’ operator and then using ‘//’ operator.  For example: 
# average1= (player1+ player2+player3)/3 # average using  ‘/’ operator
 #average2= (player1+player2+player3)//3 # average using ‘//’ operator
 #Explain your observations. Remove the parenthesis from the equations and print average1 and average2 again.  Give screenshots of the code, outputs and the git repository


from MyGameVersion2 import winner1
from MyGameVersion2 import winner2
from MyGameVersion2 import winner3


Avarage1=(winner1+winner2+winner3)/3
print("the avarage1 with () is "+str(Avarage1))
Avarage2 = (winner1+winner2+winner3)//3
print("the avarage2 with () is "+str(Avarage2))

Avarage1=winner1+winner2+winner3/3
print("the avarage1 without () is "+str(Avarage1))
Avarage2 =winner1+winner2+winner3//3
print("the avarage2 without () is "+str(Avarage2))
 

