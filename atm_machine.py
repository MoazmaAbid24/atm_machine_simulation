# ATM Machine Simulation

PIN = "1234"
balance = 0.0  # Initial account balance

# Function to check balance
def check_balance():
    print(f"💰 Your current balance is: ${balance:.2f}")

# Function to deposit money
def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"✅ ${amount:.2f} deposited successfully!")
        check_balance()
    else:
        print("⚠️ Invalid amount!")

# Function to withdraw money
def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: $"))
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"✅ ${amount:.2f} withdrawn successfully!")
            check_balance()
        else:
            print("❌ Insufficient balance!")
    else:
        print("⚠️ Invalid amount!")

# Main ATM loop
def atm_machine():
    pin_attempt = input("Enter your 4-digit PIN: ")
    if pin_attempt != PIN:
        print("❌ Incorrect PIN! Access denied.")
        return
    
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("👋 Thank you! Exiting ATM...")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

# Run the ATM
if __name__ == "__main__":
    atm_machine()
