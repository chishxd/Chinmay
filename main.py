import random
import time

def setNum():
    return random.randint(1,10)
def Accbalance(winner,i = 0,j = 0):
    balance = 10000
    if winner == 1:
        balance += 2*i
    if winner == 0:
        balance -= i
    if j > 0:
        balance += i
    return balance
    
while True:
    answer = setNum()
    print("Welcome to Ring! Fellow Warrior")
    time.sleep(1)
    bet = int(input("Place your Bet! The Number should be between 1 - 10 only! "))
    time.sleep(2)
    amt = int(input("How Much money are you willing to pay? "))
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
        balance = Accbalance(1,amt)
        print(balance)
    else:
        print("Marda, kay aasa. Ya parat")
        balance = Accbalance(0,0,amt)
    if balance == 0:
        addbal = int(input("Bhava Paishe smplet ki... Ghaal aani: "))
    print(balance)
    e = input("Press E to exit: ").lower()
    if e == "e":
        break