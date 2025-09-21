import random

def spin_row():
    numbers = ['1', '7', '9', '0', '5']

    return [random.choice(numbers) for number in range(3)]
    
def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '1':
            return bet *2
        elif row[0] == '7':
            return bet *20
        elif row[0] == '9':
            return bet *5
        elif row[0] == '0':
            return bet *3
        elif row[0] == '5':
            return bet *10
        else:
            return 0
    return 0

def main():
    

    balance = int(input("Cash in an amount to bet:$ "))
    
    print("*******************")
    print("Python Slot Machine.")
    print("------Have Fun!------")
    print("*******************")
    
    while balance > 0:
        print(f"Your current balance ${balance}")
        
        bet = (input("Enter amount of bet:$ "))

        if not bet.isdigit():
            print("Please enter a valid input")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        
        balance -= bet

        row = spin_row()
        print("Spinning. . .\n")
        print_row(row)

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again (Y/N): ").upper()

        if play_again != 'Y':
            break

if __name__ == "__main__":
    main()