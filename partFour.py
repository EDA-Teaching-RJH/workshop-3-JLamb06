username = ("admin")
password = ("password123")

URusername = input("Enter your password: ")
URpassword = input("Enter your password: ")

if URusername == username and URpassword == password:
    print("Access Granted")
else:
    print("Access Denied")