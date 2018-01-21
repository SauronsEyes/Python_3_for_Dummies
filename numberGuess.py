import numpy as np
randAns=np.random.randint(10)
print randAns
userGuess=input("Guess the number sir")
life=3
while userGuess!=randAns:
    if userGuess>randAns:
        print("HIGH")
    else:
        print("LOW")
    life=life-1
    print("LIFE REMAINING:"+str(life))
    userGuess=input("Try Again Sir")
    if life<=0:
        print("Sorry you lose")
        winCheck=False
        break
if winCheck==True:
    print("Perfectly Guessed")
else:
    print("You lost all the Life")
