#!/usr/bin/env python3
"""
Demo script for Banking Management System.
This script demonstrates the key features of the banking system.
"""

from banking_system import BankingSystem
from account import Account

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def main():
    """Run the banking system demo."""
    print_section("BANKING MANAGEMENT SYSTEM - DEMO")
    
    # Initialize the banking system
    bank = BankingSystem('demo_data.json')
    
    # Demo 1: Create customers
    print_section("1. Creating Customers")
    alice = bank.create_customer(
        "Alice Smith",
        "alice@example.com",
        "555-1234",
        "123 Main Street"
    )
    print(f"Created customer: {alice.name}")
    print(f"Customer ID: {alice.customer_id}")
    
    bob = bank.create_customer(
        "Bob Johnson",
        "bob@example.com",
        "555-5678",
        "456 Oak Avenue"
    )
    print(f"\nCreated customer: {bob.name}")
    print(f"Customer ID: {bob.customer_id}")
    
    # Demo 2: Create accounts
    print_section("2. Creating Accounts")
    alice_checking = bank.create_account(
        alice.customer_id,
        Account.CHECKING,
        5000.0
    )
    print(f"Created checking account for {alice.name}")
    print(f"Account Number: {alice_checking.account_number}")
    print(f"Initial Balance: ${alice_checking.balance:.2f}")
    
    alice_savings = bank.create_account(
        alice.customer_id,
        Account.SAVINGS,
        10000.0
    )
    print(f"\nCreated savings account for {alice.name}")
    print(f"Account Number: {alice_savings.account_number}")
    print(f"Initial Balance: ${alice_savings.balance:.2f}")
    
    # Demo 3: Perform transactions
    print_section("3. Performing Transactions")
    
    print(f"Depositing $2,000 into Alice's checking...")
    bank.deposit(alice_checking.account_number, 2000.0)
    print(f"New Balance: ${alice_checking.balance:.2f}")
    
    print(f"\nWithdrawing $500 from Alice's checking...")
    bank.withdraw(alice_checking.account_number, 500.0)
    print(f"New Balance: ${alice_checking.balance:.2f}")
    
    # Demo 4: Check balance
    print_section("4. Checking Balances")
    balance = bank.check_balance(alice_checking.account_number)
    print(f"Alice's checking account balance: ${balance:.2f}")
    
    balance = bank.check_balance(alice_savings.account_number)
    print(f"Alice's savings account balance: ${balance:.2f}")
    
    # Demo 5: Transaction history
    print_section("5. Transaction History")
    transactions = bank.get_transaction_history(alice_checking.account_number)
    print(f"Transactions for account {alice_checking.account_number}:")
    for i, txn in enumerate(transactions, 1):
        print(f"\n{i}. {txn}")
    
    # Demo 6: Update customer information
    print_section("6. Updating Customer Information")
    print(f"Current phone: {alice.phone}")
    bank.update_customer(alice.customer_id, phone="555-9999")
    updated_alice = bank.get_customer(alice.customer_id)
    print(f"Updated phone: {updated_alice.phone}")
    
    # Demo 7: List customer accounts
    print_section("7. Listing Customer Accounts")
    accounts = bank.get_customer_accounts(alice.customer_id)
    print(f"Accounts for {alice.name}:")
    for i, acc in enumerate(accounts, 1):
        print(f"\n{i}. {acc}")
    
    # Demo 8: Error handling
    print_section("8. Error Handling Demo")
    try:
        print("Attempting to withdraw $1,000,000 (should fail)...")
        bank.withdraw(alice_checking.account_number, 1000000.0)
    except ValueError as e:
        print(f"✓ Error caught correctly: {e}")
    
    try:
        print("\nAttempting to deposit -$100 (should fail)...")
        bank.deposit(alice_checking.account_number, -100.0)
    except ValueError as e:
        print(f"✓ Error caught correctly: {e}")
    
    print_section("DEMO COMPLETED SUCCESSFULLY")
    print("\nData has been saved to demo_data.json")
    print("Run this script again to see data persistence in action!")

if __name__ == "__main__":
    main()
