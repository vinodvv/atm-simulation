import os

def atm_simulation():
    balance = float(100)
    print("\nWelcome to ATM!")
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Please enter correct option from the menu (i.e., 1 to 4).")
            continue

        if option == 1:
            print(f"Current Balance: INR {balance}")
        
        elif option == 2:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Please enter an amount greater than zero.")
                    continue

                balance += amount
                print(f"Deposit successful! Your new balance is: INR {balance}")
            except ValueError:
                print("Invalid input!")
        
        elif option == 3:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Please enter an amount greater than zero.")
                    continue
                if amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful! Your new balance is: INR {balance}")
            except ValueError:
                print("Invalid input!")
        elif option == 4:
            print("Thank you for using ATM. Goodbye!")
            break

        else:
            print("Invalid input! Please enter correct option from the menu (i.e., 1 to 4).")


if __name__ == "__main__":
    atm_simulation()
