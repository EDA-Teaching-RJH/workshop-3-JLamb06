age = int(input("How old are you? "))
if age > 0 and age < 18:
    print("You are a child")
elif age > 0 and age >= 18:
    print("You are an adult")
else:
    print ("You dont exist")

