import random

guessed = False

secret_number = random.randint(1,10)

while guessed == False:
    number = int(input("Guess a number between 1 and 10. "))
    if number == secret_number:
        print("You guessed the number!")
        guessed = True
    else:
        print("You didn't guess correctly")


