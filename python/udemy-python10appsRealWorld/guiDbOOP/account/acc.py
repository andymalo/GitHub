class Account:
    """
    Classe de compte
    """

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        """
        Retrait d'argent
        """
        self.balance = self.balance - amount

    def deposit(self, amount):
        """
        Dépot d'argent
        """
        self.balance = self.balance + amount

    def commit(self):
        """
        MAJ du fichier
        """
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """
    C'est çà une doc strings
    """

    type = "checking account"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfert(self, amount):
        """
        Transfert d'argent
        """
        self.balance = self.balance - amount - self.fee

jacks_account = Checking("account//jack.txt", 1)
print(jacks_account.balance)
jacks_account.transfert(100)
print(jacks_account.balance)
jacks_account.commit()
print(jacks_account.type)

john_account = Checking("account//john.txt", 1)
print(john_account.balance)
john_account.transfert(200)
print(john_account.balance)
john_account.commit()
print(john_account.type)

print(john_account.__doc__)