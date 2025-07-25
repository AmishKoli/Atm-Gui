class Atm:
    __counter=1
    def __init__(self):

        self.__pin = ""
        self.__balance = 0
        self.__menu()
        self.sno=Atm.counter
        Atm.__counter+=1
    @staticmethod
    def get_counter():
        return Atm.__counter
    @staticmethod
    def set_counter(new):
        if type(new)== int:
            Atm.__counter=new
        else:
            print("Not Allowed")
    def __menu(self):
        user_input = input("""
                    Hello, how would you like to proceed?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")
            
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successfully")
        self.__menu()
        
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
        self.__menu()
    
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Operation successful")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
        self.__menu()
    
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
        
