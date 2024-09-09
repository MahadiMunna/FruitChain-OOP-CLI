class Account:
    def __init__(self, name, password, email, address, account_type) -> None:
        self.name=name
        self.password=password
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=0
        self.transaction=[]
        self.loan_times=0
        self.acc_no = len(brac.acc_list)+20230
        brac.acc_list.append(self)

    def deposit(self, amount):
        self.balance+=amount
        brac.total_balance+=amount
        msg=f"{amount} tk added to your account successfully."
        print(msg)
        self.transaction.append("Deposit - "+msg)

    def withdraw(self, amount):
        if brac.loan_status=='on' and (self.balance >= amount and amount>0):
            self.balance-=amount
            brac.total_balance-=amount
            msg=f"Your withdrwal amount is {amount} and your new balance is {self.balance}"
            print(msg)
            self.transaction.append("Withdraw - "+msg)
        else:
            if amount==0:
                print("You can't withdraw 0tk!\n")
            elif brac.loan_status=='off':
                print("--->Bank is currently Bankrupt! Withdraw service is currently off!!")
            else:
                print("Withdrawal amount exceeded!\n")
    def check_balance(self):
        print(f"Your current balance is {self.balance}")
    def transaction_history(self):
        for i,val in enumerate(self.transaction):
            print(i+1,f". {val}")
    def take_loan(self,amount):
        if brac.loan_status=="on" and self.loan_times<2:
            msg=f"Congratualtions! You got {amount}tk loan from bank and added to your account!"
            print(msg)
            self.transaction.append("loan - "+msg)
            self.balance+=amount
            brac.total_loan+=amount
            brac.total_balance-=amount
            self.loan_times+=1
        else:
            if brac.loan_status=='off':
                print("--->Bank is currently Bankrupt! Loan service is currently off!!")
            else:
                print("You can't take loan, you already take 2 times.")
    def transfer_balance(self, acc_no, amount):
        if amount<self.balance and amount>99:
            receiver=None
            for account in brac.acc_list:    
                if account.acc_no==acc_no:
                    receiver=account
                    break
            if receiver==None:
                print("Account does not exixt!\n")
            else:
                receiver.balance+=amount
                receiver.transaction.append(f"Receive - {amount} tk received from {currentUser.name}!")
                currentUser.balance-=amount
                currentUser.transaction.append(f"Send - {amount} tk send to {receiver.name}!")
                print(f"Money sucessfully transfer to {receiver.name}\' bank account!")
        else:
            if amount<99:
                print("\n---->You can't transfer less than 100tk!")
            else:
                print("\n---->You don't have enough money to send<----\n")
     

class Bank:
    def __init__(self, total_balance, total_loan, loan_status) -> None:
        self.total_balance=total_balance
        self.total_loan=total_loan
        self.loan_status=loan_status
        self.acc_list=[]
    def delete_account(self, acc_no):
        user=False
        for account in brac.acc_list:
            if account.acc_no==acc_no:
                user=True
                brac.acc_list.remove(account)
                print(f"Acount no {acc_no} successfully deleted!\n")
                break
        if user==False:
            print("No user found with this account number!\n")
    def show_users(self):
        print("\nUsers list:")
        if len(brac.acc_list)==0:
            print("User list is empty!")
        else:
            for i,val in enumerate(self.acc_list):
                print(i+1,f". Name: {val.name}, Account No: {val.acc_no}, Email: {val.email}, Address: {val.address}")
        print("\n\n")
    def show_total_balance(self):
        print(f"\nCurrent Bank balance is {self.total_balance}\n")
    def show_total_loan(self):
        print(f"\nTotal Loan given {self.total_loan}\n")
    def set_loan_status(self,status):
        self.loan_status=status
        print(f"\n----->Loan status successfully set {status}!!\n")

# Main program
brac = Bank(100000,0,'on')
currentUser=None

while(True):

    op=int(input("\n---->BRAC Bank Ltd.<------\n1. Admin\n2. User\n3. Exit\n\nEnter your option: "))
    if op==1:
        print("Admin login - (Use 'admin' for username and password)\n")
        name=input("Username: ")
        password=input("Password: ")
        if name=='admin' and password=='admin':
            print("\n------>Welcome Admin to BRAC Bank Ltd.<--------\n")
            while True:
                op=int(input("---->Menu<-------\n1. Create an account\n2. Delete an user account\n3. User accounts list\n4. Cheack bank balance\n5. Check total loan\n6. Change loan status\n7. Logout\n\nEnter your option: "))
                if(op==1):
                    print("Provide user information: ")
                    name=input("Name: ")
                    pas=input("Password: ")
                    email=input("Email: ")
                    add=input("Address: ")
                    acc_type=input("Account type(savings/cuurent) : ")
                    
                    user=Account(name,pas,email,add,acc_type)
                    print(f"\nSuccessfully account created! \n\nAccount number: {user.acc_no}\nPassword: {user.password}\n\nProvide this account number and password to the user. It will need when user will try to login.\n")
                elif(op==2):
                    acc_no=int(input("Enter account Number:"))
                    brac.delete_account(acc_no)
                    
                elif(op==3):
                    brac.show_users()
                elif(op==4):
                    brac.show_total_balance()
                elif(op==5):
                    brac.show_total_loan()
                elif(op==6):
                    status=input("What is the present loan status(on/off): ")
                    brac.set_loan_status(status)
                elif(op==7):
                    break
                else:
                    print('Enter a valid option!')
        else:
            print("Incorrect username or password!\n")
    elif op==2:
        x=int(input("1. Register\n2. Login\n\nEnter your option: "))
        if x==1:
            print("Provide us about your information: ")
            name=input("Name: ")
            pas=input("Password: ")
            email=input("Email: ")
            add=input("Address: ")
            acc_type=input("Account type(savings/cuurent) : ")
            
            currentUser=Account(name,pas,email,add,acc_type)
            print(f"Successfully registered! Your account number is {currentUser.acc_no} and remember your password for future!\n\n---->Welcome to BRAC Bank {currentUser.name}!<----")
            while True:
                op=int(input("\n---->Menu<----\n\n0. User profile\n1. Deposit\n2. withdraw\n3. Balance\n4. Transactions\n5. Take loan\n6. Transfer Balance\n7. Logout\n\nEnter your option: "))
                if op==0:
                    print(f"\nUserName: {currentUser.name}\nAccount No: {currentUser.acc_no}\nEmail: {currentUser.email}\nAddress: {currentUser.address}\nAccount Type: {currentUser.account_type}\n")
                
                elif(op==1):
                    amount=int(input("Enter amount for deposite: "))
                    currentUser.deposit(amount)
                elif(op==2):
                    amount=int(input("Enter amount for withdraw: "))
                    currentUser.withdraw(amount)
                elif(op==3):
                    currentUser.check_balance()
                elif(op==4):
                    currentUser.transaction_history()
                elif(op==5):
                    amount=int(input("Enter amount for loan: "))
                    currentUser.take_loan(amount)
                elif(op==6):
                    acc_no=int(input("Enter receiver account number: "))
                    amount=int(input("Enter amount for transfer: "))
                    currentUser.transfer_balance(acc_no,amount)
                elif(op==7):
                    break
                else:
                    print('Enter a valid option!')
        else:
            acc_no=int(input("Enter account Number:"))
            for account in brac.acc_list:
                
                if account.acc_no==acc_no:
                    currentUser=account
                    break
            if currentUser==None:
                print("Enter a valid account number!")
            else:
                pas=input("Enter password: ")
                if currentUser.password==pas:
                    print(f"\n--->Welcome {currentUser.name}!<----")
                    while True:
                        op=int(input("\n---->Menu<----\n\n0. User profile\n1. Deposit\n2. withdraw\n3. Balance\n4. Transactions\n5. Take loan\n6. Transfer Balance\n7. Logout\n\nEnter your option: "))
                        if op==0:
                            print(f"\nUserName: {currentUser.name}\nAccount No: {currentUser.acc_no}\nEmail: {currentUser.email}\nAddress: {currentUser.address}\nAccount Type: {currentUser.account_type}\n")
                        if(op==1):
                            amount=int(input("Enter amount for deposite: "))
                            currentUser.deposit(amount)
                        elif(op==2):
                            amount=int(input("Enter amount for withdraw: "))
                            currentUser.withdraw(amount)
                        elif(op==3):
                            currentUser.check_balance()
                        elif(op==4):
                            currentUser.transaction_history()
                        elif(op==5):
                            amount=int(input("Enter amount for loan: "))
                            currentUser.take_loan(amount)
                        elif(op==6):
                            acc_no=int(input("Enter receiver account number: "))
                            amount=int(input("Enter amount for transfer: "))
                            currentUser.transfer_balance(acc_no,amount)
                        elif(op==7):
                            break
                        else:
                            print('Enter a valid option!')
    elif op==3:
        break
    else:
        print("Invalid option choosen!")

    