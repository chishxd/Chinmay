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
    time.sleep(0)
    amt = int(input("How Much money are you willing to pay? "))
    if amt < newbal:
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
            print("sattta jinklas ki bhava! Laav aani paishe")
            newbal = balance.win_bal(amt)
        else:
            print("Marda, kay aasa. Ya parat")
            newbal = balance.lose_bal(amt)
        if newbal == 0:
            addbal = int(input("Bhava Paishe smplet ki... Ghaal aani: "))
            newbal = balance.add_bal(addbal)
        print(newbal)
    else:
        print("This Amount is not available on the account")
    e = input("Press E to exit: ").lower()
    if e == "e":
        break
