"""Main application interface for the Banking Management System."""

from banking_system import BankingSystem
from account import Account

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def print_menu():
    """Print the main menu."""
    print_header("BANKING MANAGEMENT SYSTEM - MAIN MENU")
    print("\n1.  Customer Management")
    print("2.  Account Management")
    print("3.  Deposit Money")
    print("4.  Withdraw Money")
    print("5.  Check Balance")
    print("6.  Transaction History")
    print("7.  Exit")
    print("\n" + "-" * 60)

def customer_menu():
    """Print customer management menu."""
    print_header("CUSTOMER MANAGEMENT")
    print("\n1.  Create New Customer")
    print("2.  View Customer Details")
    print("3.  Update Customer Details")
    print("4.  List All Customers")
    print("5.  Back to Main Menu")
    print("\n" + "-" * 60)

def account_menu():
    """Print account management menu."""
    print_header("ACCOUNT MANAGEMENT")
    print("\n1.  Create New Account")
    print("2.  View Account Details")
    print("3.  View Customer Accounts")
    print("4.  Back to Main Menu")
    print("\n" + "-" * 60)

def handle_customer_management(bank):
    """Handle customer management operations."""
    while True:
        customer_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            # Create new customer
            print_header("CREATE NEW CUSTOMER")
            name = input("Enter customer name: ").strip()
            email = input("Enter email: ").strip()
            phone = input("Enter phone: ").strip()
            address = input("Enter address: ").strip()
            
            if name and email and phone and address:
                customer = bank.create_customer(name, email, phone, address)
                print(f"\n✓ Customer created successfully!")
                print(f"Customer ID: {customer.customer_id}")
            else:
                print("\n✗ Error: All fields are required!")
        
        elif choice == '2':
            # View customer details
            print_header("VIEW CUSTOMER DETAILS")
            customer_id = input("Enter Customer ID: ").strip()
            customer = bank.get_customer(customer_id)
            
            if customer:
                print(f"\n{customer}")
            else:
                print("\n✗ Customer not found!")
        
        elif choice == '3':
            # Update customer details
            print_header("UPDATE CUSTOMER DETAILS")
            customer_id = input("Enter Customer ID: ").strip()
            customer = bank.get_customer(customer_id)
            
            if customer:
                print(f"\nCurrent details:\n{customer}")
                print("\nEnter new details (press Enter to keep current value):")
                
                name = input(f"Name [{customer.name}]: ").strip()
                email = input(f"Email [{customer.email}]: ").strip()
                phone = input(f"Phone [{customer.phone}]: ").strip()
                address = input(f"Address [{customer.address}]: ").strip()
                
                if bank.update_customer(customer_id, name or None, email or None, 
                                       phone or None, address or None):
                    print("\n✓ Customer details updated successfully!")
                else:
                    print("\n✗ Error updating customer!")
            else:
                print("\n✗ Customer not found!")
        
        elif choice == '4':
            # List all customers
            print_header("ALL CUSTOMERS")
            customers = bank.list_customers()
            
            if customers:
                for i, customer in enumerate(customers, 1):
                    print(f"\n{i}. {customer}")
                    print("-" * 60)
            else:
                print("\nNo customers found!")
        
        elif choice == '5':
            break
        
        else:
            print("\n✗ Invalid choice! Please try again.")

def handle_account_management(bank):
    """Handle account management operations."""
    while True:
        account_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            # Create new account
            print_header("CREATE NEW ACCOUNT")
            customer_id = input("Enter Customer ID: ").strip()
            customer = bank.get_customer(customer_id)
            
            if not customer:
                print("\n✗ Customer not found!")
                continue
            
            print(f"\nCustomer: {customer.name}")
            print("\nAccount Types:")
            print(f"1. {Account.CHECKING}")
            print(f"2. {Account.SAVINGS}")
            
            acc_type_choice = input("\nSelect account type: ").strip()
            account_type = Account.CHECKING if acc_type_choice == '1' else Account.SAVINGS
            
            try:
                initial_deposit = float(input("Enter initial deposit (0 or more): ").strip() or 0)
                if initial_deposit < 0:
                    print("\n✗ Initial deposit cannot be negative!")
                    continue
                
                account = bank.create_account(customer_id, account_type, initial_deposit)
                print(f"\n✓ Account created successfully!")
                print(f"Account Number: {account.account_number}")
                print(f"Account Type: {account.account_type}")
                print(f"Initial Balance: ${account.balance:.2f}")
            except ValueError:
                print("\n✗ Invalid amount!")
        
        elif choice == '2':
            # View account details
            print_header("VIEW ACCOUNT DETAILS")
            account_number = input("Enter Account Number: ").strip()
            account = bank.get_account(account_number)
            
            if account:
                customer = bank.get_customer(account.customer_id)
                print(f"\n{account}")
                print(f"Customer: {customer.name if customer else 'Unknown'}")
            else:
                print("\n✗ Account not found!")
        
        elif choice == '3':
            # View customer accounts
            print_header("VIEW CUSTOMER ACCOUNTS")
            customer_id = input("Enter Customer ID: ").strip()
            customer = bank.get_customer(customer_id)
            
            if not customer:
                print("\n✗ Customer not found!")
                continue
            
            accounts = bank.get_customer_accounts(customer_id)
            
            if accounts:
                print(f"\nAccounts for {customer.name}:")
                for i, account in enumerate(accounts, 1):
                    print(f"\n{i}. {account}")
                    print("-" * 60)
            else:
                print(f"\nNo accounts found for {customer.name}")
        
        elif choice == '4':
            break
        
        else:
            print("\n✗ Invalid choice! Please try again.")

def handle_deposit(bank):
    """Handle deposit operation."""
    print_header("DEPOSIT MONEY")
    account_number = input("Enter Account Number: ").strip()
    account = bank.get_account(account_number)
    
    if not account:
        print("\n✗ Account not found!")
        return
    
    print(f"\nAccount: {account_number}")
    print(f"Current Balance: ${account.balance:.2f}")
    
    try:
        amount = float(input("\nEnter deposit amount: ").strip())
        transaction = bank.deposit(account_number, amount)
        
        if transaction:
            print(f"\n✓ Deposit successful!")
            print(f"Amount Deposited: ${amount:.2f}")
            print(f"New Balance: ${account.balance:.2f}")
            print(f"Transaction ID: {transaction.transaction_id}")
    except ValueError as e:
        print(f"\n✗ Error: {e}")
    except Exception as e:
        print(f"\n✗ Error: {e}")

def handle_withdrawal(bank):
    """Handle withdrawal operation."""
    print_header("WITHDRAW MONEY")
    account_number = input("Enter Account Number: ").strip()
    account = bank.get_account(account_number)
    
    if not account:
        print("\n✗ Account not found!")
        return
    
    print(f"\nAccount: {account_number}")
    print(f"Current Balance: ${account.balance:.2f}")
    
    try:
        amount = float(input("\nEnter withdrawal amount: ").strip())
        transaction = bank.withdraw(account_number, amount)
        
        if transaction:
            print(f"\n✓ Withdrawal successful!")
            print(f"Amount Withdrawn: ${amount:.2f}")
            print(f"New Balance: ${account.balance:.2f}")
            print(f"Transaction ID: {transaction.transaction_id}")
    except ValueError as e:
        print(f"\n✗ Error: {e}")
    except Exception as e:
        print(f"\n✗ Error: {e}")

def handle_balance_check(bank):
    """Handle balance check operation."""
    print_header("CHECK BALANCE")
    account_number = input("Enter Account Number: ").strip()
    balance = bank.check_balance(account_number)
    
    if balance is not None:
        account = bank.get_account(account_number)
        customer = bank.get_customer(account.customer_id)
        print(f"\nAccount Number: {account_number}")
        print(f"Account Type: {account.account_type}")
        print(f"Customer: {customer.name if customer else 'Unknown'}")
        print(f"Current Balance: ${balance:.2f}")
    else:
        print("\n✗ Account not found!")

def handle_transaction_history(bank):
    """Handle transaction history viewing."""
    print_header("TRANSACTION HISTORY")
    account_number = input("Enter Account Number: ").strip()
    
    try:
        limit_input = input("Enter number of recent transactions (press Enter for all): ").strip()
        limit = int(limit_input) if limit_input else None
        
        transactions = bank.get_transaction_history(account_number, limit)
        
        if transactions is None:
            print("\n✗ Account not found!")
            return
        
        if transactions:
            account = bank.get_account(account_number)
            print(f"\nTransaction History for Account: {account_number}")
            print(f"Current Balance: ${account.balance:.2f}")
            print("\n" + "-" * 60)
            
            for i, transaction in enumerate(transactions, 1):
                print(f"{i}. {transaction}")
        else:
            print("\nNo transactions found!")
    except ValueError:
        print("\n✗ Invalid input!")

def main():
    """Main application entry point."""
    bank = BankingSystem()
    
    print_header("WELCOME TO BANKING MANAGEMENT SYSTEM")
    print("\nA simple and efficient application for managing banking operations")
    
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            handle_customer_management(bank)
        elif choice == '2':
            handle_account_management(bank)
        elif choice == '3':
            handle_deposit(bank)
        elif choice == '4':
            handle_withdrawal(bank)
        elif choice == '5':
            handle_balance_check(bank)
        elif choice == '6':
            handle_transaction_history(bank)
        elif choice == '7':
            print_header("THANK YOU")
            print("\nThank you for using the Banking Management System!")
            print("Goodbye!\n")
            break
        else:
            print("\n✗ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
