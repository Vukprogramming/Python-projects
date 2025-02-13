#Python Telecommunications

print('Welcome to Python Telecommunications!')

print("A phone number cannot contain more or less than 9 digits")
number = input("Enter your phone number: ")

while len(number) != 9 or not number.isdigit():
    if len(number) != 9:
        print("Number needs to contain exactly 9 characters.")
    elif not number.isdigit():
        print("Phone number must contain only digits.")
    number = input("Enter your phone number: ")

print(f"Your phone number is: {number}")

credit = 0  

while True:
    
    print("1. Message")
    print("2. Check credit")
    print("3. Add credit")
    print("4. Exit")
    
    answer = input("Enter your choice: ")

    if answer == '1':
        
        numba = input("Enter a number to message: ")

        message = input("Enter your message: ")

        while len(numba) != 9 or not numba.isdigit():
            if len(numba) != 9:
                print("Number needs to contain exactly 9 characters.")
            elif not numba.isdigit():
                print("Phone number must contain only digits.")
            numba = input("Enter a valid 9-digit phone number to message: ")

        
        if credit <= 0:
            print("Not enough credit to send the message.")
        elif credit <= 5:
            print("Your credit is low (less than or equal to 5). Please add more credit.")
        else:
            
            credit -= 1  
            print(f"Message sent to {numba}. Your remaining credit is {credit}.")

    elif answer == '2':
        
        print(f"You have {credit} $ of credit")

    
        
    elif answer == "3":
        
        while True:
            amount = input("Enter how much you want to add to your credit: ")

            if amount.isdigit():
                amount = int(amount)
                (amount) += (credit)
                print(f"Added {amount} to your credit")
                break
            else:
                print("Invalid amount")