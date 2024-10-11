num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator1 = input("Enter the operator: ")
tf = False

while tf == False:
    match operator1:
        case "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            tf = True
        case "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            tf = True
        case "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            tf = True
        case "/":
            if num1 == 0 or num2 == 0:
                print("You may not divide by 0")
                tf = True
            else: 
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                tf = True
        case "^":
            result = num1 ^ num2
            print(f"{num1} ^ {num2} = {result}")
            tf = True
        case "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
            tf = True
        case "quit":
            print("Quitting the application")
            break

        

