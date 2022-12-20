from random import *
while True:
    x = randint(0,1) 
    y = randint(0,1)
    
    Guess =  input("enter your guess: ")
    Guess = int(Guess)

    if (Guess == x) :
        print("correct")
    
    elif(Guess == y) :
        print("correct")
    
    else :
        print("wrong")        
