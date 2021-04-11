import random
from datetime import datetime 

database = {}

def init():
    print("Welcome to Bank Bona \n \n")
    haveAccount = int(input("Do you have an account with us? \n 1 (Yes) \n 2 (No) \n \n"))

    if(haveAccount == 1):
        login()
        
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected an invalid option \n \n")
        init()

def login():
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginSuccessful = True
                    
                    bankOperation(userDetails)
                else: 
                    print("Invalid account or password")
            else: 
                print("Invalid account or password")
            

def register():
    print("******* Register ******** \n")
    email = input("What is your email address? \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("Create a new password \n")
    # confirmPassword = input("Confirm your password \n")
    accountNumber = generateAccountNumber()

    database[accountNumber] = [email, firstName, lastName, password]
    
    print("Your account has been created")
    print("**** *********  ***********  ********")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("**** *********  ***********  ********")

    login()

def bankOperation(user):
    currentTime = datetime.now().time()
    currentDate = datetime.now().strftime('%y-%m-%d')
    print("Welcome %s %s!!!" % (user[1], user[2]))
    print("Date: %s" %currentDate)
    print("Time: %s" %currentTime)

    selectedOption = int(input("What do you want to do? \n (1) deposit \n (2) withdraw \n (3) complaint \n (4) logout \n (5) exit \n"))
    
    if(selectedOption == 1):       
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()      
    elif(selectedOption == 3):
        complaint()
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)
    

def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit")

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def complaint():
    complaint = input("What issue will you like to complain about? \n")
    print("Your complaint: %s \n Has been received" %complaint )
    print("Thank you for contacting us.")

def logout():
    login()

init()

