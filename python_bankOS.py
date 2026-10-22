import os
import sys
import getpass
from bank_function import show_balance, deposite_money, witdraw_money

# --- Account Setup ---
stored_pin = "12345"
account_name = "Dawood"
attempts_left = 3
balance = 50000.0
authenticated = False

# Function to clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#--- FUNTION TO HIDE THE PIN
def mask_input(prompt="Enter PIN: "):
    print(prompt, end="", flush=True)
    pin = ""
    while True:
        try:
            #---TO HIDE PIN IN WINDOWS\LINUX
            pin=getpass.getpass("")
            break
        except Exception:
            pin=input()
            break
    return pin

clear_screen()
print("=" * 45)
print("        WELCOME TO PYTHON BANK ATM        ")
print("=" * 45)
            
# --- Security Check ---
while attempts_left > 0:
    entered_pin = mask_input(f"\nEnter your PIN ({attempts_left} Attempts Left): ")
    
    if entered_pin == stored_pin:
        authenticated = True
        print(f"\n--> Success! Welcome, {account_name}!")
        input("\nPress Enter to access main menu...")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print("--> Incorrect PIN. Try again!")

if not authenticated:
    print("\n" + "!" * 45)
    print("SECURITY ALERT: Card Blocked (3 Failed Attempts)")
    print("!" * 45)

# --- Main ATM Interface Loop ---
while authenticated:
    clear_screen()
    print("=" * 45)
    print(f" Account: {account_name} | Status: Active")
    print("=" * 45)
    print(" 1. Check Balance")
    print(" 2. Withdraw Money")
    print(" 3. Deposit Money")
    print(" 4. Exit")
    print("=" * 45)
    
    choice = input("\nSelect an option (1-4): ")

    if choice == "1":
        show_balance(balance)
        input("\nPress Enter to return to main menu...")

    elif choice == "2":
        # --- FAST CASH WITHDRAWAL ---
        clear_screen()
        print("=" * 45)
        print("            Withdrawal Menu")
        print("=" * 45)
        print(" 1. $500")
        print(" 2. $1000")
        print(" 3. $2000")
        print(" 4. $5000")
        print(" 5. Custom / Other Amount")
        print(" 6. Back to Main Menu")
        print("=" * 45)

        withdraw_choice = input("\nSelect an option (1-6): ").strip()

        if withdraw_choice == "1":
            balance = witdraw_money(balance, 500.0)
            input("\nPress ENTER to return to Main Menu...")
        elif withdraw_choice == "2":
            balance = witdraw_money(balance, 1000.0)
            input("\nPress ENTER to return to Main Menu...")
        elif withdraw_choice == "3":
            balance = witdraw_money(balance, 2000.0)
            input("\nPress ENTER to return to Main Menu...")
        elif withdraw_choice == "4":
            balance = witdraw_money(balance, 5000.0)
            input("\nPress ENTER to return to Main Menu...")
        elif withdraw_choice == "5":
            try:
                custom_amount = float(input("\nEnter custom amount: $"))
                if custom_amount > 0:
                    balance = witdraw_money(balance, custom_amount)
                else:
                    print("--> ERROR! Amount must be greater than 0.")
            except ValueError:
                print("--> ERROR! Invalid input. Enter numbers only.")
            input("\nPress ENTER to return to Main Menu...")
        elif withdraw_choice == "6":
            pass
        else:
            print("--> Invalid selection!")
            input("\nPress ENTER to try again...")

    elif choice == "3":
        # Bulletproof Deposit Loop
        while True:
            try:
                deposit_amount = float(input("\nEnter Deposit Amount: $"))
                if deposit_amount <= 0:
                    print("--> ERROR! Amount must be greater than 0.")
                    continue
                balance = deposite_money(balance, deposit_amount)
                break
            except ValueError:
                print("--> ERROR! Invalid Input. Enter numbers only (e.g. 50, 100).")

        input("\nPress ENTER to return to Main Menu...")

    elif choice == "4":
        clear_screen()
        print("=" * 45)
        print(f"Thank you for banking with us, {account_name}!")
        print("Have a great day!")
        print("=" * 45)
        break
        
    elif choice == "4":
        clear_screen()
        print("=" * 45)
        print(f"Thank you for banking with us, {account_name}!")
        print("Have a great day!")
        print("=" * 45)
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")
        input("\nPress Enter to try again...") 