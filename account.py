

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