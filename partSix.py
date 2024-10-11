age = int(input("How old are you? "))
student = input("Are you a student? ")

if (student == "yes" or student == "Yes") and (age < 65 or age >= 12):
    print("The ticket will be £8")
elif age >= 65 or age < 12 and age > 0:
    print("The ticket will be £5")
elif (student == "no" or student == "No") and (age <= 64 or age >= 12):
    print("The ticket will be £10")
else:
    print("You're not born yet")