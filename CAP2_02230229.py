
import random

class Bank_Account:
    def __init__(self, Account_Number, Account_Type, Balance=0.00):
        self.Account_Number= Account_Number
        self.Account_Type = Account_Type
        self.Balance = Balance

    def Deposit_Money(self,Input_Amount):
        self.Balance += Input_Amount

    def Withdraw_Money(self,Input_Amount):
        if self.Balance >= Input_Amount:
            self.Balance -= Input_Amount
        else:
            print("Insufficient Balance")
    
    def Transfer_Money(self, Receiver, Input_Amount):
        if self.Balance >= Input_Amount:
            self.Withdraw_Money(Input_Amount)
            Receiver.Deposit_Money(Input_Amount)
        else:
            print("Insifficient Balance!!")
    
    def Delete_Account(self):
        pass
class Saving_Account(Bank_Account):
    pass
class Business_Account(Bank_Account):
    pass

def Account_Number_Generate():
    return str(random.randint(10000000000,99999999999))
def Create_New_Account(Account_Type):
    Account_Number = Account_Number_Generate()
    Password = Generate_Password()
    if Account_Type in ["Saving", "Business"]:
        Account = Saving_Account(Account_Number, Account_Type)
        with open ("accounts.txt","r") as file:
            file.write(f"{Account_Number}, {Password}, {Account_Type}, {Account.Balance}\n")
        return Account_Number, Password

def Login_Account(Account_Number, Password):
    with open ("accounts.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            if len (data)==4:
                Acc_number, Pword, Acc_type, balance =data
                Acc_number = Acc_number.strip()
                Pword = Pword.strip()
                if Acc_number == Account_Number and Pword == Password:
                    return Acc_type, float(balance)
            else:
                print("Invalid data Format:",data)    
    return None, None

def Generate_Password():
    return str(random.randint(100000,999999))

def main():
    while True:
        print("WELCOME TO OOP BANKING SYSTEM!!!")
        print("1. Create New Account\n 2. Login Account \n 3. Exit")
        option= input("Enter Your Option: ")

        if option =="1":
            Account_Type = input("Enter the Account type you want to create (Saving/Business): ")
            Account_Number, Password = Create_New_Account(Account_Type)
            if Account_Number:
                print(f"Account has been created successfully!!. \n Your Account Number is : {Account_Number} \n Your Password is: {Password}")
        elif option == "2":
            Account_Number = input("Enter your Account Number: ")
            Password=input("Enter your Password: ")
            Account_Type, Balance = Login_Account(Account_Number ,Password)
            if Account_Type:
                print(f"Login Successful, Account Type: {Account_Type}, Balance: {Balance}")
            else:
                print("Invalid Account Number Or Password!! \n Please Try Again")
        elif option == "3":
            break
        else:
            print("Invlid Option")

if __name__ == "__main__":
    main()
