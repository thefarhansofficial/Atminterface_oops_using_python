class Atm:

    def __init__(self):

        self.pin = " "
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("hello how would you like to proceed \n 1.Enter 1 to Create Pin \n 2.Enter 2 to Deposit "
                           "\n 3.Enter 3 to Withdraw \n 4.Enter 4 to Check Balance \n 5. Enter 5 to Exit\n")

        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("exit")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("pin set succesfully")

    def deposit(self):
        temp=self.pin
        if temp == self.pin:
            amount = int(input("enter the amount"))
            self.balance = self.balance + amount
            print("deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("operation succesfull")
            else:
                print("Insufficient funds")
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
