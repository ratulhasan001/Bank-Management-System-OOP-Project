from account import Account
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