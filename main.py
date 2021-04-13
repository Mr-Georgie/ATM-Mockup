import random
import datetime
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d, %H:%M:%S")

database = {}

# function to start application
def init():
    
    print("***WELCOME TO Pydroid Bank***")
    print("The current date and time is: ", date_time, "\n")

    print("Do you have an account with us?")
    print("Press '1' for Yes")
    print("Press '2' for No")
    print("Press '3' to exit")
    
    have_account=int(input("Enter your answer: "))
        
    if have_account == 1:
        login()
    elif have_account==2:
        register()
    elif have_account==3:
        exit()
    else:
        print("Invalid Option Selected")
        init() 
        
#main operations of the app
def register():
    print("***** Registration Portal*****")

    first_name=input("Enter your First Name: ")
    last_name=input("Enter your Last Name: ")
    e_mail=input("Enter your Email address:")
    password=input("Create your passsword: ")

    account_number = generate_random_number()
    card_number = generate_random_number()
    balance = 0
    database[account_number]=[first_name,last_name,e_mail,password,card_number,balance]
    
    print("Your account has been successfully created")
    print(f"Your account number is: {account_number}")
    print("Make sure to deposit into your account to make it active")
    
    login()

def login():
    print("\n")
    print("***************LOGIN******************")
    print("Please enter your Account Number to login")
    user_account_number = int(input('Your response: '))
    
    if user_account_number in database.keys():
        print('Account number recognized')
        user_password = input('Enter your secret password: ')
        for user_details in database.values():
            if user_password == user_details[3]:
                print("\n")
                print( "Login Successful")
                print(f'Welcome {user_details[0]} {user_details[1]}\n')
                banking_operations(user_details)
            else:
                print("Invalid password.. Try again")
                print("Press 1 to try again")
                print("Press 2 to exit")
                response = int(input("Your response: "))
                if response == 1:
                    login()
                else:
                    exit()
    else:
        print("Invalid Acount Number")
        print("Press 1 to try again")
        print("Press 2 to exit")
        response = int(input("Your response: "))
        if response == 1:
            login()
        else:
            exit()

def logout():
    print("\n")
    print("Logout Successful")
    print("\n")
    init()
    
def exit():
    print("Bye for now... Do come back again sometime")


### user related operations
def banking_operations(user):

    print('What would you like to do?')
    print("Press '1' to deposit")
    print("Press '2' to withdraw")
    print("Press '3' for complaint")
    print("Press '4' for check balance")
    print("Press '5' to logout")
    print("Press '6' to exit")
    
    options = int(input("Enter your answer: "))
    
    if options == 1:
        deposit(user)
    elif options == 2:
        withdrawal(user)
    elif options == 3:
        customer_care(user)
    elif options == 4:
        balance_equiry(user)
    elif options == 5:
        logout()
    elif options == 6:
        exit()
    else:
        print("Invalid option selected")
        banking_operations(user)

def withdrawal(user):
    print("\n")
    print("***Withdrawal***")
    amount = int(input(("How much would you like to withdraw?\n")))
    if user[-1] == 0:
        print("Your balance is empty. Please make deposits")
    elif user[-1] < amount: 
        print("Insufficient funds. Make more deposits")
    else:
        user[-1] -= amount
        print(f"Take your cash: {amount}")
        print(f"Your balance is {user[-1]}")
    
    banking_operations(user)

def balance_equiry(user):
    print(f"Your balance is {user[-1]}")
    banking_operations(user)

def deposit(user):
    print("\n")
    print("***Deposit***")
    amount = int(input("How much would you like to deposit?\n"))
    user[-1] += amount
    
    print(f"Your deposit of {amount} has been confirmed.")
    banking_operations(user)

def customer_care(user):
    print('This is the Customer Care Unit')
    complaint = input("What isssue would you like to report?\n")
    print("Your complaint has been registered. You'll be contacted shortly")
    print("Thank you")
    banking_operations(user)


# To generate random numbers for account number and card number

def generate_random_number():
    return random.randrange(0000000000,9999999999)

# start the app
init()