class Account():
    """A class to represent a single bank account"""

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        """checks for valid inputs: password and positive amount, then adds to balance amount
        """
        if password != self.password:
            print("Sorry incorrect password")
            return None
        
        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None
        
        self.balance = self.balance + amountToDeposit
        return self.balance
    
    def withdraw(self, amountToWithdraw, password):
        """Checks for appropiate funds before allowing user to get money"""
        if password != self.password:
            print("Sorry incorrect password")
            return None
        
        if amountToWithdraw < 0:
            print("You cannot deposit a negative amount")
            return None
        
        if amountToWithdraw > self.balance:
            print(f"You do not have enough funds to withdraw {amountToWithdraw}")

        self.balance = self.balance - amountToWithdraw
        return self.balance
    
    def getBalance(self, password):
        """Allows the user to see how much money is in their account"""
        if password != self.password:
            print("Sorry incorrect password")
            return None

        return self.balance
    
    