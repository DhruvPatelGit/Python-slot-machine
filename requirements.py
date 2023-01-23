MAX_LINES=3
MAX_BET=100
MIN_BET=1
def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Number of Lines must be in between 1 and",MAX_LINES)
        else:
            print("Please enter a number.")
        
    return lines
            
def get_bet():
    while True:
        amount=input("Enter the amount you would like to bet on each line : $")
        if amount.isdigit():
            amount = int(amount)
            if amount>=MIN_BET:
                if amount<=MAX_BET:
                    break
                else:
                    print("Bet amount should be less than",MAX_BET)
            else:
                print("Minimum bet amount should be",MIN_BET)
        else:
            print("Please enter a number.")
    return amount
