class BankAccount:
    def __init__(self,name:str , balance:float):
        self.name = name
        self.balance = balance

    def deposit(self,amount:float):
        if amount > 0:
            self.balance += amount
        else:
            print("your amount is 0")

        return f'You make a deposit with {amount}'

    def withdraw(self,requested_amount:float):

        if requested_amount <= self.balance:
            print("Your withdraw is successful the requested amount is", requested_amount, "and your account balance is", (self.balance - requested_amount))
        else:
            print("your withdraw amount: ", requested_amount, "is greater than your balance" ,self.balance)
        
    def display_balance(self):
        print("Your account balance is: ",self.balance)
    
class UserSelection(BankAccount):
    def __init__(self, name: str, balance: float):
        super().__init__(name, balance)
                       
    def selection(self):
        select = int(input("Choose the process you want:\n1- Deposit\n2- Withdraw\n3- Display Balance\n"))

        match select:
            case 1:
                amount = float(input("please enter the amount you need to deposit: "))
                print(self.deposit(amount)) 
            case 2:
                amount = float(input("please enter the amount you need to withdraw: "))
                print(self.withdraw(amount))
            case 3:
                print(self.display_balance())


if __name__ == "__main__":
    # Create an instance of UserSelection with an initial name and balance
    user_account = UserSelection("John Doe", 1000)

    # Continuously offer the menu until the user decides to exit
    while True:
        user_account.selection()
        
        # Ask the user if they want to perform another operation
        continue_choice = input("Do you want to perform another operation? (yes/no): ").lower()
        if continue_choice != "yes":
            print("Thank you for using our banking application. Goodbye!")
            break   