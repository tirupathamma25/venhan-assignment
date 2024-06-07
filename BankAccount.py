class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposite(self):
        print("amount: {}".format(self.balance + 5000))
        
    def withdraw(self):
        with_draw_money = 10000
        remaining_money = self.balance - with_draw_money
        if (with_draw_money + remaining_money == self.balance):
            print("True")
        else:
            print("False")
        
    def get_balance(self):
        print("current Balance: {}".format(self.balance))
       
        
b = BankAccount("23133431", "Tirupathamma", 20000.0)

b.deposite()
b.withdraw()
b.get_balance()
  