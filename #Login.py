#Login

print("Welcome to PGD!")

answer = input("Enter 1 to make an account, or enter 2 to exit: ")

while answer not in ["1", "2"]:
    print("That is not a valid choice.")
    answer = input("Enter 1 to make an account, or enter 2 to exit: ")

if answer == "1":
    username = input("Enter a username: ")
    
    while len(username) < 5:
        print("Username cannot contain less than 5 characters.")
        username = input("Enter a username: ")
    
    while len(username) > 10:
        print("Username cannot contain more than 10 characters.")
        username = input("Enter a username: ")
    
    password = input("Enter a password: ")

    while len(password) < 5:
        print("Password cannot contain less then 5 characters")
        password = input("Enter a password: ")

    while len(password) > 15:
        print("Password cannot contain more than 15 characters")
        password =  input("Password can only contain digits. Enter a password: ")

if answer == "2":
    print("Have a nice day!")
    quit()

rre = input("Your account is set up. Press 1 to continue or press 2 to exit: ")

if rre == "2":
    print("Have a nice day!")

if rre == "1":
    print("To continue you need to log into your account")

answer = input("Enter your username: ")

while answer not in {username}:
    print("Incorrect username:")
    answer = input("Enter your username: ")

answer = input("Enter your password: ")

while answer not in {password}:
    print("Incorrect password")
    answer = input("Enter your password: ")

    print("Your done have a great day.")
