class bankAccount:
  def__init__(self,account_number,account_holder_name,initial_balance=0.0):
Self.__account_number=account_number
self.account__holder_name=account_holder_name
self.account__balance=initial_balance

def deposit(self,amount):
  if amount >0:
    self.__account_balance+=amount
    print("Deposited  {}.new balance: {}.format(amount,self.__account_balance))

  else:
    print("invaid deposit amount.please deposit a positive  amount.")

def withdrew(self,amount):
  if amount>0 and amount<=self.__account_balance:
    self.__account_balance-=amount
    print("withdrew   {}. new balance:  {}".format(amount,self.__account_balance))  

  else:
    print("invalid withdrew amount or  insufficient balance.")

def  dislay_balance(self):
  print{"Account balance for {} (Account #{}):  {}".format(
    self.__account_holder_name,self.__account_number,
    self.__account_balance))


account=bankAccount(account_number="13245567",account_holder_name="sweetha",initial_balance=500000)

account.display_balance()
account.deposit(500.0)
account.withdrew(200.0)
account.display_balance()