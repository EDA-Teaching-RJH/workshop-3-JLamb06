day = input("Enter a day of the week: ")

if day == "saturday" or day == "Saturday" or day == "Sunday" or day == "sunday":
    print("It's the weekend")
elif day == "Monday" or day == "monday" or day == "Tuesday" or day == "tuesday" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "thursday" or day == "Friday" or day == "friday":
    print("It's a weekday") 
else:
    print("Thats not a day of the week")
