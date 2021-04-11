import random
from datetime import datetime 

database = {4363657467: ["bona@gmail.com", "bona", "chukwudi", "1234567", 3567]}

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
                    currentTime = datetime.now().time()
                    currentDate = datetime.now().strftime('%y-%m-%d')
                    print("Welcome %s %s!!!" % (userDetails[1], userDetails[2]))
                    print("Date: %s" %currentDate)
                    print("Time: %s" %currentTime)

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

    database[accountNumber] = [email, firstName, lastName, password, 0]
    
    print("Your account has been created")
    print("**** *********  ***********  ********")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("**** *********  ***********  ********")

    login()

def bankOperation(user):
    selectedOption = int(input("What do you want to do? \n (1) deposit \n (2) withdraw \n (3) balance \n (4) complaint \n (5) logout \n (6) exit \n"))
    
    if(selectedOption == 1):       
        depositOperation(user)
    elif(selectedOption == 2):
        withdrawalOperation(user)      
    elif(selectedOption == 3):
        balance(user)      
    elif(selectedOption == 4):
        complaint()
    elif(selectedOption == 5):
        logout()
    elif(selectedOption == 6):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)
    

def withdrawalOperation(user):
    print("Your available balance is %d" % (user[4]))
    withdrawal = int(input("How much do you want to withdraw? \n"))

    if(withdrawal < user[4]):
        print("Your withdrawal of %d was successful" % (withdrawal))
        dep = user[4] - withdrawal
        print("Your current balance is %d \n" % (dep))

        bankOperation(user)
    else: 
        print("Your balance is so small.... Please make a deposit")
        bankOperation(user)

def depositOperation(user):
    deposit = int(input("How much do you want to deposit? \n"))

    if(deposit > 0):
        print("Your deposit of %d was successful" % (deposit))
        dep = deposit + user[4]
        print("Your current balance: %d \n" % (dep))
        
        bankOperation(user)


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def complaint():
    complaint = input("What issue will you like to complain about? \n")
    print("Your complaint: %s \n Has been received" %complaint )
    print("Thank you for contacting us.")

def balance(user):
    print("**** *********  ***********  ********")
    print("Your current balance is %d" % user[4])
    print("**** *********  ***********  ********")
    bankOperation(user)

def logout():
    login()

init()

