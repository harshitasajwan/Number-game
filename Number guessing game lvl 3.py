import random
num=random.randint(1,100)
attempts=5
print("WELCOME TO NUMBER GUESSING GAME")
print("(you only have 5 guesses )")
while True:
    guess = int(input("GUESS A NUMBER FROM 1 TO 100:\n"))
    attempts-=1
    #checking guess
    if (guess==num):
        print(f"Wohoooooo!! you've got the right guess on your {attempts}attempt")
    elif (guess>num):
        print("Guess is greater than the number")
    else:
        print("Guess is too small")
    #adding a little drama!!
    if(attempts==5):
        print("5 ATTEMPTS,got a long way to go buddy")
    elif(attempts==4):
        print("4 ATTEMPTS LEFT,they got you there.")
    elif(attempts==3):
        print("3 ATTEMPTS LEFT,GUESS CAREFULLY.")
    elif(attempts==2):
        print("2 ATTEMPTS LEFT.\nUSE YOUR BRAIN A LITTLE.")
    elif(attempts==1):
        print("LAST CHANCE NO GOING BACK,IT'S A DO OR DIE SITUATION\nRAISE YOUR SWORD AND RUN TOWARDS YOUR VICTORY MY CHILD")
    else:
        print("GAME OVER!!BETTER LUCK NEXT TIME THE NUMBER WAS ",num)
        break
        


#added a little drama

        