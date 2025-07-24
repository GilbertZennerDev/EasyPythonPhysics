#Objects : Encapsulation

class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number # "Private" attributes with double underscores
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self): # Method to securely retrieve the balance
        return self.__balance

# Create an Account object
my_account = Account("DE123456789", 1000)

# Direct access (not strictly enforced by Python, but it's the convention)
# print(my_account.__balance) # This would cause an error!

# Access and manipulation via methods
print(f"Current balance: {my_account.get_balance()}")
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(2000) # Attempt to withdraw more than available
my_account.deposit(-100) # Attempt to deposit a negative amount
print(f"Final balance: {my_account.get_balance()}")
print(my_account.__balance) #show the error
