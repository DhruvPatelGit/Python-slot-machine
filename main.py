from deposit import deposit
from spin import spin

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        temp=input("Press enter to spin (q to quit).")
        if temp == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")

main()