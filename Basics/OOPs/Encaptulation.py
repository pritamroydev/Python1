class BankAccount:

    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.__balance = balance            # __balance -> these "__" signify that it is a private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposited amount: {amount}. New Balance: {self.__balance}')

    def getbalance(self):                               # a 'getter' method to access the private variable
        print(f'Current Balance: {self.__balance}')


account1 = BankAccount("12345", 50000)

account1.getbalance()
account1.deposit(3000)

# print(account1.__balance)       -> will print no such balance exists(you can't access the private variable directly)