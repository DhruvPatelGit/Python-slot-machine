from requirements import get_number_of_lines,get_bet
from slot_machine import get_slot_machine_spin,check_winnings,print_slot_machine

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def spin(balance):
    lines=get_number_of_lines()
    quit=0
    while True:
        bet=get_bet()
        total_bet=bet*lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount.")
            quit=1
            break
        else:
            break
    
    if(quit==0):
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")    
        slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
        print_slot_machine(slots)
        winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
        print(f"You won ${winnings}.")
        print(f"You won on lines:",*winning_lines)
    else:
        winnings=0
        total_bet=0


    return winnings-total_bet
    