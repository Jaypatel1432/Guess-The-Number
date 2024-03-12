import random

randnum = random.randint(1,100)
print(randnum)
usernum =None
guess = 0

while(usernum!=randnum):
    usernum  = int(input("Enter the number :- "))
    if (usernum>randnum):
        print("your number is bigger than random number")
    elif(usernum == randnum):
        print("congratulations! , your guessed it right!")
    else:
        print("your number is smaller than random number")

    guess = guess+1
print("_______GAME OVER_______")
print(f"you guessed the number in {guess} guesses")

with open("highscore.txt","r") as f:
    highscore = f.read()

if highscore =="":
    print("you have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guess))

elif guess < int(highscore):
    print("you have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guess))

