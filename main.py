from account import *
from admin import *

def main(): # done
 
    bank = Admin("World Bank")
    admin = bank.create_an_account("admin","adminErMail.com","admin")
    
    user_status = admin
    changing_user = None

    while True: 
 
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