"""Demo script showcasing Banking Management System functionality."""

from bank import Bank
from account import Account
from customer import Customer


def demo():
    """Run a demonstration of the Banking Management System."""
    print("="*60)
    print("BANKING MANAGEMENT SYSTEM - DEMO")
    print("="*60)
    
    # Create a bank
    bank = Bank("MyBank Demo")
    print(f"\n✓ Created bank: {bank.bank_name}")
    
    # Create customers
    print("\n--- Creating Customers ---")
    customer1 = bank.create_customer(
        "John Doe",
        "john.doe@email.com",
        "555-1234",
        "123 Main St, City"
    )
    
    customer2 = bank.create_customer(
        "Jane Smith",
        "jane.smith@email.com",
        "555-5678",
        "456 Oak Ave, Town"
    )
    
    # Create accounts
    print("\n--- Creating Accounts ---")
    account1 = bank.create_account("John Doe", 5000.0)
    account2 = bank.create_account("Jane Smith", 3000.0)
    account3 = bank.create_account("Bob Johnson", 0.0)
    
    # Perform some transactions
    print("\n--- Performing Transactions ---")
    print("\n• Depositing $1500 to John's account:")
    account1.deposit(1500.0)
    
    print("\n• Withdrawing $800 from Jane's account:")
    account2.withdraw(800.0)
    
    print("\n• Depositing $2000 to Bob's account:")
    account3.deposit(2000.0)
    
    print("\n• Attempting to withdraw $10000 from John's account (insufficient funds):")
    account1.withdraw(10000.0)
    
    print("\n• Depositing $500 to Jane's account:")
    account2.deposit(500.0)
    
    # Display account information
    print("\n--- Account Details ---")
    account1.display_account_info()
    
    # Display transaction history
    print("\n--- Transaction History for John's Account ---")
    account1.display_transactions()
    
    # Display customer information
    print("\n--- Customer Details ---")
    customer1.display_info()
    
    # Update customer information
    print("\n--- Updating Customer Information ---")
    customer1.update_phone("555-9999")
    customer1.update_email("john.new@email.com")
    
    # Display updated customer info
    customer1.display_info()
    
    # List all accounts
    bank.list_all_accounts()
    
    # List all customers
    bank.list_all_customers()
    
    # Display bank summary
    bank.display_bank_summary()
    
    # Check balances
    print("\n--- Final Balances ---")
    print(f"John's balance: ${account1.get_balance():.2f}")
    print(f"Jane's balance: ${account2.get_balance():.2f}")
    print(f"Bob's balance: ${account3.get_balance():.2f}")
    
    print("\n" + "="*60)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("="*60)


if __name__ == "__main__":
    demo()
