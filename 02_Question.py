class account:
     def __init__(self,bal,acc):
          self.balnace=bal
          self.account_no=acc
          
     def debit(self,Amount):
          self.balnace -= Amount
          print("Rs",Amount,"was debited")
        #  print("total balance",self.gat_banlance())
          print(self.balnace)
          
     def crebit(self,Amount):
          self.balnace += Amount
          print("Rs",Amount,"was credit")
         # print("total balance",self.gat_banlance())
          print(self.balnace)

          
     # def gat_banlance(self):
     #  return self.balnace    

acc1=account(12500,1381000)
print(acc1.balnace)
print(acc1.account_no)
acc1.debit(2000)
acc1.crebit(56852)
