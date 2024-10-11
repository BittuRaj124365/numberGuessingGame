# By using random module to generate random characters

import random
target=random.randint(1,100)
print("Hint:- Press Quit/quit to quit the Game: ")
while(True):
    userChoise=input("Guess the Target-->")
    if(userChoise=="Quit" or userChoise=="quit"):
        print("...You decided to quit the Game....")
        break
    userChoise=int(userChoise)
    if(userChoise==target):
        print("Succes: Correct Guess!!")
        break
    elif(userChoise>target):
        print("Its Too big, Guess smaller one. ")
    else:   #(userChoise<target)
        print("Its too small, Guess bigger one. ")
print("---->GameOver<----")