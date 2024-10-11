truefalse = False

while truefalse == False:

    score = int(input("Enter the score of your test: "))

    if score >= 90 and score <=100:
        print("You got an A")
        break
    elif score >= 80 and score <=89:
        print("You got an B")
        break
    elif score >= 70 and score <=79:
        print("You got an C")
        break
    elif score >= 60 and score <=69:
        print("You got an D")
        break
    elif score >= 0 and score <=60:
        print("You got an F")
        break
    elif score > 100:
        print("Thats too many marks, try again")
    else:
        print("Thats not enough marks. try again")
    