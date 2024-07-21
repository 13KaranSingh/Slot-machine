MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = int(input("Enter amount to be deposited: $"))
        if amount > 0:
            break
        else:
            print("Please enter a valid amount!")

    return amount



def get_number_of_lines():
    while True:
        lines = int(input("Enter amount to of lines to bet on(1-" + str(MAX_LINES) + ")? "))
        if 1 <= lines <= MAX_LINES:
            break
        else:
            print("Please enter a valid number of lines")

    return lines


def get_bet():
    while True:
        amount = int(input("How much do you want to bet on each line: $"))
        if MIN_BET <= amount <= MAX_BET:
            break
        elif balance < amount:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            print(f"Please enter a valid amount, amount must be between ${MIN_BET} - ${MAX_BET}!")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

main()

        
