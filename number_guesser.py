import random
import time

class Balance:
    def __init__(self, balance = 10000):
        self.balance = balance
    def win_bal(self, amount):
        self.balance += 2 * amount
        return self.balance
    def lose_bal(self, amount):
        self.balance -= amount
        return self.balance
    def add_bal(self, amount):
        self.balance += amount
        return self.balance
def setNum():
    return random.randint(1,10)

balance = Balance()
while True:
    newbal = balance.balance
    answer = setNum()
    print("Welcome to Ring! Fellow Warrior")
    time.sleep(1)
    bet = int(input("Place your Bet! The Number should be between 1 - 10 only! "))
    if bet > 10:
        bet = input("Please enter a valid bet: ")
        amt = int(input("How Much money are you willing to pay? "))
        if amt > newbal:
            print("This Amount is not available on the account")
        else:
            time.sleep(0.5)
            print("Well said, Now")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print(f"The Number is.... {answer}!!")
            if bet == answer:
                print(f"Contrats! You won {2*amt}")
                newbal = balance.win_bal(amt)
            else:
                print("Ohh... You Lost! Better Luck Next Time!")
                newbal = balance.lose_bal(amt)
            if newbal == 0:
                addbal = int(input("You are out of money, add more balance to you A/C: "))
                newbal = balance.add_bal(addbal)
            print(newbal)
    else:
        amt = int(input("How Much money are you willing to pay? "))
        if amt > newbal:
            print("This Amount is not available on the account")
        else:
            time.sleep(0.5)
            print("Well said, Now")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print(f"The Number is.... {answer}!!")
            if bet == answer:
                print(f"Contrats! You won {2*amt}")
                newbal = balance.win_bal(amt)
            else:
                print("Ohh... You Lost! Better Luck Next Time!")
                newbal = balance.lose_bal(amt)
            if newbal == 0:
                addbal = int(input("You are out of money, add more balance to you A/C: "))
                newbal = balance.add_bal(addbal)
            
        end = input('''Press 1/balance to check balance\nPress 2/end to exit: ''').lower().strip()
        if end in ("1", "balance"):
            print(f"Current Balance: {newbal}")
        if end == "end":
            print("See You Around!")
            break
        
