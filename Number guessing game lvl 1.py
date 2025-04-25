import random
num=random.randint(1,100)
print("WELCOME TO NUMBER GUESSING GAME")
while True:
    guess = int(input("GUESS A NUMBER FROM 1 TO 100:\n"))

    if (guess==num):
        print("Wohoooooo!! You guessed it right!!")
    elif (guess>num):
        print("Guess is greater than the number")
    else:
        print("Guess is too small")
    
        
#normal game

