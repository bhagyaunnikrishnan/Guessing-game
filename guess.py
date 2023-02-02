import random
number = random.randint(1,100)
print("This is a number guessing game!!")
print("Rules..\n1.You should choose a number between 1 and 100\n2.You have only 10 chances")
player_name = input("Hello, What's your name?")
tries = 0
print("Okay!" + player_name +"\nNow I am guessing a number between 1 and 100:\nLet's start guessing the numbers..")
while tries < 10:
    guess = int(input())
    tries = tries + 1
    if guess > number:
        print("Your guess is too high")
    if guess < number:
        print("Your guess is too low")
    if guess == number:
        break
if guess == number:
    print("You won the game and guessed the number in " + str(tries) + " tries!")
else:
    print("You did not guess the number correctly, The number was " + str(number) +"\nYou lost the game!\nPlay again..")
