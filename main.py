class Admin:
    '''
    requirements    done 
    create   done
    delete done
    show all users done
    total balance show done
    total loan  done
    onloan done
    offloan done
    '''
    def __init__(self, name): # done
        self.accounts = []
        self.name = name
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True
    
    def create_an_account(self, name, email, type): # done
        account = Account(name, email, type)
        self.accounts.append(account)
        return account
    
    def delete_an_account(self, account_number): # done
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                del account
                return
        print(f'Deletion Failed! No account found with number {account_number}!')
        
    def show_all_users_list(self): # done
        for account in self.accounts:
            print(f'Account User : {account.name}    Account Number : {account.account_number}')
    
    def show_total_balance(self): # done
        print(f"Tolal Available Balance: {self.total_balance}")
    
    # loan section 
    def show_total_loan(self): # done
        print(f"Current Tolal Loan: {self.total_loan_amount}")
 
    def OnLoan(self): 
        self.loan_feature = True

    def OffLoan(self): 
        self.loan_feature = False

class Account: # done
    '''
    requirements
    balance 
    bank transfer
    deposit
    withdraw
    loan naoa
    transictions history
    
    
    '''
    account_number_generate = 0
    
    def __init__(self, name, email, type): # done
        self.name = name
        self.email = email
        Account.account_number_generate += 1
        self.account_number = Account.account_number_generate
        self.type = type
        self.transactions = []
        self.balance = 0
        self.loan_count = 0
        self.loan_amount = 0
        self.transaction_id = self.account_number * 10000
        
        
    def balance_check(self): # done
        print(f"Name: {self.name}")
        print(f"Account No: {self.account_number}")
        print(f"Balance: {self.balance}")
    
    def bank_transfer(self, bank, account_no, amount): # done
        for account in bank.accounts:
            if account_no == account.account_number:
                other = account
                if self.balance >= amount:
                    self.balance -= amount
                    other.balance += amount
                    print(f"{amount}$ transferred from {self.name} to {other.name}")
                    transaction = {}
                    self.transaction_id += 1
                    transaction['id'] = self.transaction_id
                    transaction['type'] = "bank_transfer"
                    transaction['from'] = self.name
                    transaction['to'] = other.name
                    transaction['amount'] = amount
            
                    self.transactions.append(transaction)

                else:
                    print("Sorry Your Current Balance is lower than the amount you entered!")
                
                return
        print(f'{account_no} Account does not exist')
                
        
        
    
    def deposit(self,bank,amount): # done
        if amount>0:
            bank.total_balance+=amount
            self.balance+=amount
            
            transaction={}
            self.transaction_id+=1
            transaction['id']=self.transaction_id
            transaction['type']="deposit"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
            
        else:
            print(f"Invalid amount !")
        
    
    def withdraw(self,bank,amount): # done
        if amount > 0 and bank.total_balance >= amount and self.balance >= amount:
            bank.total_balance-=amount
            self.balance-=amount
            
            transaction={}
            transaction['id']=self.transaction_id+1
            transaction['type']="withdraw"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
            
        else:
            print(f"Withdrawal amount exceeded!")
    
    
    def takeLoan(self,bank,amount): # done
        if bank.loan_feature == True and amount > 0 and bank.total_balance >= amount and self.loan_count < 3:
            self.loan_amount+=amount
            self.loan_count+=1
            bank.total_loan_amount+=amount
            transaction={}
            self.transaction_id+=1
            transaction['id']=self.transaction_id
            transaction['type']="loan"
            transaction['amount']=amount
            self.transactions.append(transaction)
        
        else:
            print(f'Invalid Loan Request !')
    
    def transictions_history(self): # done
        print(f"Transaction History of {self.name}:")
        
        for transaction in self.transactions:
            if 'to' in transaction:
                print(f"{transaction['id']}: {transaction['type']} of taka {transaction['amount']} to {transaction['to']}")
            
            elif 'id' in transaction:
                print(f"{transaction['id']}: {transaction['type']} of taka {transaction['amount']}")


def main(): # done
 
    bank = Admin("World Bank")
    admin = bank.create_an_account("ADMIN","adminErMail.com","ADMIN")
    
    user_status = admin
    changing_user = True

    while True: # ai section tai ratin vai code theke help niye sajaisi.. hossilo na first e
 
        if user_status == None: # done
            print("No user detected")

            option = input("Login or Register ? L for Login R for Register ")

            if option == "L":
                id = int(input("Please Enter Your Account Number: "))


                ok = False
                for user in bank.accounts:
                    if user.account_number==id:
                        user_status=user
                        changing_user=True
                        ok=True
                        break
                if ok == False:
                    print("No user Found ! Please Login in Valid Way")

            elif option == "R":
                name=input("Please Enter Your Name:")
                email=input("Please Enter Your E-mail:")
                type=input("Account Type (Savings/Current):")

                user=bank.create_an_account(name,email,type)

                user_status=user
                changing_user=True

        else: # done
            if changing_user:
                print(f"User Name :  {user_status.name} !")
                changing_user=False
            else:
                print("Operation Ended!")

            if user_status.name == "admin": # done
 
                print("Options:")
                print("1: Create an Account")
                print("2: Delete an Existing Account")
                print("3: Show All Users")
                print("4: Check Total Balance")
                print("5: Check Total Loan")
                print("6: Turn On Loan facility")
                print("7: Turn Off Loan facility")
                print("8: Log Out")


                ch=int(input("Choose the option :"))

                if ch == 1:
                    name=input("Enter Name:")
                    email=input("Enter E-mail:")
                    type=input("Account Type (Savings/Current):")

                    bank.create_an_account(name,email,type)

                elif ch == 2:
                    account_no=int(input("Enter Account Number:"))
                    bank.delete_an_account(account_no)


                elif ch == 3:
                    bank.show_all_users_list()

                elif ch == 4:
                    bank.show_total_balance()

                elif ch == 5:
                    bank.show_total_loan()

                elif ch == 6:
                    bank.OnLoan()

                elif ch == 7:
                    bank.OffLoan()

                elif ch == 8:
                    user_status = None

                else:
                    print(" Invalid Input Given")


            else: # done
                print("Options: ")
                print("1: Deposit an Amount")
                print("2: Withdraw an Amount")
                print("3: Check Total Balance")
                print("4: Check All Transactions History")
                print("5: Take Loan")
                print("6: Tarnsfer an Amount")
                print("7: Logout")

                ch=int(input("Choose the option :"))

                if ch == 1:
                    amount=int(input("Enter Amount:"))
                    user_status.deposit(bank,amount)

                elif ch == 2:
                    amount=int(input("Enter Amount:"))
                    user_status.withdraw(bank,amount)

                elif ch == 3:
                    user_status.balance_check()

                elif ch == 4:
                    user_status.transictions_history()


                elif ch == 5:
                    amount=int(input("Enter Amount:"))
                    user_status.takeLoan(bank,amount)

                elif ch == 6:
                    account_no = int(input("Enter an Valid Account to Transfer Money:"))
                    amount=int(input("Enter total Amount of Money:"))

                    user_status.bank_transfer(bank,account_no,amount)

                elif ch == 7:
                    user_status=None

                else:
                    print(" Invalid Input Given")
                    
if __name__ == '__main__':
    main()