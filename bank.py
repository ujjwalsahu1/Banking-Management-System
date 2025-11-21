"""Bank module for managing multiple accounts and customers."""

from typing import Dict, Optional, List
from account import Account
from customer import Customer


class Bank:
    """Represents a bank managing multiple accounts and customers."""
    
    def __init__(self, bank_name: str):
        """Initialize a new bank.
        
        Args:
            bank_name: Name of the bank
        """
        self.bank_name = bank_name
        self.accounts: Dict[str, Account] = {}
        self.customers: Dict[str, Customer] = {}
        self.next_account_number = 1000
        self.next_customer_id = 1
    
    def create_customer(self, name: str, email: str, phone: str, address: str = "") -> Customer:
        """Create a new customer.
        
        Args:
            name: Customer's full name
            email: Customer's email address
            phone: Customer's phone number
            address: Customer's address (optional)
            
        Returns:
            Created Customer object
        """
        customer_id = f"CUST{self.next_customer_id:04d}"
        self.next_customer_id += 1
        
        customer = Customer(customer_id, name, email, phone, address)
        self.customers[customer_id] = customer
        
        print(f"\nCustomer created successfully!")
        print(f"Customer ID: {customer_id}")
        return customer
    
    def create_account(self, customer_name: str, initial_balance: float = 0.0) -> Optional[Account]:
        """Create a new account.
        
        Args:
            customer_name: Name of the account holder
            initial_balance: Starting balance (default: 0.0)
            
        Returns:
            Created Account object or None if failed
        """
        try:
            account_number = f"ACC{self.next_account_number:06d}"
            self.next_account_number += 1
            
            account = Account(account_number, customer_name, initial_balance)
            self.accounts[account_number] = account
            
            print(f"\nAccount created successfully!")
            print(f"Account Number: {account_number}")
            print(f"Customer Name: {customer_name}")
            print(f"Initial Balance: ${initial_balance:.2f}")
            return account
        except ValueError as e:
            print(f"Error creating account: {e}")
            return None
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """Get an account by account number.
        
        Args:
            account_number: Account number to retrieve
            
        Returns:
            Account object or None if not found
        """
        return self.accounts.get(account_number)
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get a customer by customer ID.
        
        Args:
            customer_id: Customer ID to retrieve
            
        Returns:
            Customer object or None if not found
        """
        return self.customers.get(customer_id)
    
    def delete_account(self, account_number: str) -> bool:
        """Delete an account.
        
        Args:
            account_number: Account number to delete
            
        Returns:
            True if successful, False otherwise
        """
        if account_number not in self.accounts:
            print(f"Error: Account {account_number} not found")
            return False
        
        account = self.accounts[account_number]
        if account.balance > 0:
            print(f"Error: Cannot delete account with non-zero balance (${account.balance:.2f})")
            return False
        
        del self.accounts[account_number]
        print(f"Account {account_number} deleted successfully")
        return True
    
    def list_all_accounts(self):
        """Display all accounts in the bank."""
        if not self.accounts:
            print("\nNo accounts found.")
            return
        
        print("\n" + "="*80)
        print(f"{self.bank_name} - ALL ACCOUNTS")
        print("="*80)
        print(f"{'Account Number':<15} {'Customer Name':<25} {'Balance':<15} {'Transactions'}")
        print("-"*80)
        
        for acc_num, account in sorted(self.accounts.items()):
            balance_str = f"${account.balance:.2f}"
            print(f"{account.account_number:<15} {account.customer_name:<25} "
                  f"{balance_str:<15} {len(account.transactions)}")
        
        print("="*80)
        print(f"Total Accounts: {len(self.accounts)}")
    
    def list_all_customers(self):
        """Display all customers in the bank."""
        if not self.customers:
            print("\nNo customers found.")
            return
        
        print("\n" + "="*80)
        print(f"{self.bank_name} - ALL CUSTOMERS")
        print("="*80)
        print(f"{'Customer ID':<15} {'Name':<25} {'Email':<25} {'Phone'}")
        print("-"*80)
        
        for cust_id, customer in sorted(self.customers.items()):
            print(f"{customer.customer_id:<15} {customer.name:<25} "
                  f"{customer.email:<25} {customer.phone}")
        
        print("="*80)
        print(f"Total Customers: {len(self.customers)}")
    
    def get_total_deposits(self) -> float:
        """Calculate total deposits in the bank.
        
        Returns:
            Total amount deposited across all accounts
        """
        return sum(account.balance for account in self.accounts.values())
    
    def display_bank_summary(self):
        """Display bank summary information."""
        print("\n" + "="*50)
        print(f"{self.bank_name} - SUMMARY")
        print("="*50)
        print(f"Total Accounts: {len(self.accounts)}")
        print(f"Total Customers: {len(self.customers)}")
        print(f"Total Deposits: ${self.get_total_deposits():.2f}")
        print("="*50)
