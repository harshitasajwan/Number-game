import random
num=random.randint(1,100)
attempts=5
print("WELCOME TO NUMBER GUESSING GAME")
print("(you only have 5 guesses )")
while True:
    guess = int(input("GUESS A NUMBER FROM 1 TO 100:\n"))
    attempts-=1
    print(attempts,"attempts left")
    if (guess==num):
        print(f"Wohoooooo!! you've got the right guess on your {attempt}attempt")
    elif (guess>num):
        print("Guess is greater than the number")
    else:
        print("Guess is too small")
    if (attempts==0):
        print("GAME OVER!!BETTER LUCK NEXT TIME THE GUESS WAS ",num)
        break
        