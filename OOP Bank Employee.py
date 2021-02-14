#SEAT No. EB20102140
#NAME:UMAIR IQBAL
#BSCS(A) Evening


class BankEmployee():
  def __init__(self,Employee_Name,Employee_Position):
    self.name = Employee_Name
    self.position = Employee_Position
    self.balance = 0
  def Deposit_Amount(self,deposit_amount):
    Deposit_Amount = self.balance + deposit_amount
    self.balance = Deposit_Amount
    return 'Deposited Rs.{} to the {} {} account'.format(deposit_amount,self.position,self.name)
  def Withdraw_Amount(self,withdraw_amount):
    if withdraw_amount <= self.balance:
      self.balance = self.balance - withdraw_amount
      return 'Withdraw Rs.{} from the {} {} account'.format(withdraw_amount,self.position,self.name)
    else:
      return 'Not sufficient amount in {} {} account'.format(self.position,self.name)
  def Check_Balance(self):
    return 'Balance of {} {} account is Rs.{}'.format(self.position,self.name,self.balance)

emp1 = BankEmployee('umair','manager')

print(emp1.Check_Balance())
print(emp1.Deposit_Amount(500))
print(emp1.Withdraw_Amount(500))
print(emp1.Check_Balance())
print(emp1.Withdraw_Amount(100))
