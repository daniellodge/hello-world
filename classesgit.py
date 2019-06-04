class BankAccount():
  def __init__(self, name,balance):
    self.name = name
    self.balance = balance
  def info(self):
    print(self.name,self.balance)
  def deposit(self):
    amount=float(input("How much would you like to deposit"))
    self.balance=amount+self.balance
  def withdraw(self):
    amount1=float(input("How much would you like to withdraw"))

def main():
  done = False
  while not done:
    print("Menu")
    print("D - Do Now")
    print("Q - Quit")
    choice = input("Choice: ")
    if choice == "D":
        print("Do Now")
        arianna=BankAccount("Arianna",50)
        arianna.info()
        alejandro=BankAccount("alejandro",100)
        alejandro.info()
        arianna.deposit()
        alejandro.deposit()
        arianna.info()
        alejandro.info()
        arianna.withdraw()
        alejandro.withdraw()
    elif choice == "Q":
        print("Exiting Game!")
        done = True

main()
