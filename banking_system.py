"""Banking system class that manages all banking operations."""

import json
import os
from customer import Customer
from account import Account
from transaction import Transaction

class BankingSystem:
    """Main banking system class for managing customers and accounts."""
    
    def __init__(self, data_file='banking_data.json'):
        """
        Initialize the banking system.
        
        Args:
            data_file (str): Path to the data storage file
        """
        self.data_file = data_file
        self.customers = {}
        self.accounts = {}
        self.next_customer_id = 1
        self.next_account_number = 1000
        self.next_transaction_id = 1
        self.load_data()
    
    def generate_customer_id(self):
        """Generate a new unique customer ID."""
        customer_id = f"CUST{self.next_customer_id:06d}"
        self.next_customer_id += 1
        return customer_id
    
    def generate_account_number(self):
        """Generate a new unique account number."""
        account_number = f"ACC{self.next_account_number:08d}"
        self.next_account_number += 1
        return account_number
    
    def generate_transaction_id(self):
        """Generate a new unique transaction ID."""
        transaction_id = f"TXN{self.next_transaction_id:010d}"
        self.next_transaction_id += 1
        return transaction_id
    
    def create_customer(self, name, email, phone, address):
        """
        Create a new customer.
        
        Args:
            name (str): Customer's full name
            email (str): Customer's email address
            phone (str): Customer's phone number
            address (str): Customer's physical address
            
        Returns:
            Customer: The newly created customer
        """
        customer_id = self.generate_customer_id()
        customer = Customer(customer_id, name, email, phone, address)
        self.customers[customer_id] = customer
        self.save_data()
        return customer
    
    def get_customer(self, customer_id):
        """
        Get a customer by ID.
        
        Args:
            customer_id (str): Customer ID
            
        Returns:
            Customer: The customer object or None if not found
        """
        return self.customers.get(customer_id)
    
    def update_customer(self, customer_id, name=None, email=None, phone=None, address=None):
        """
        Update customer details.
        
        Args:
            customer_id (str): Customer ID
            name (str, optional): New name
            email (str, optional): New email
            phone (str, optional): New phone
            address (str, optional): New address
            
        Returns:
            bool: True if successful, False if customer not found
        """
        customer = self.get_customer(customer_id)
        if customer:
            customer.update_details(name, email, phone, address)
            self.save_data()
            return True
        return False
    
    def list_customers(self):
        """
        Get all customers.
        
        Returns:
            list: List of all customers
        """
        return list(self.customers.values())
    
    def create_account(self, customer_id, account_type, initial_deposit=0.0):
        """
        Create a new account for a customer.
        
        Args:
            customer_id (str): Customer ID
            account_type (str): Type of account (CHECKING or SAVINGS)
            initial_deposit (float, optional): Initial deposit amount
            
        Returns:
            Account: The newly created account or None if customer not found
        """
        if customer_id not in self.customers:
            return None
        
        account_number = self.generate_account_number()
        account = Account(account_number, customer_id, account_type, 0.0)
        
        if initial_deposit > 0:
            transaction_id = self.generate_transaction_id()
            account.deposit(initial_deposit, transaction_id)
        
        self.accounts[account_number] = account
        self.save_data()
        return account
    
    def get_account(self, account_number):
        """
        Get an account by account number.
        
        Args:
            account_number (str): Account number
            
        Returns:
            Account: The account object or None if not found
        """
        return self.accounts.get(account_number)
    
    def get_customer_accounts(self, customer_id):
        """
        Get all accounts for a customer.
        
        Args:
            customer_id (str): Customer ID
            
        Returns:
            list: List of accounts belonging to the customer
        """
        return [acc for acc in self.accounts.values() if acc.customer_id == customer_id]
    
    def deposit(self, account_number, amount):
        """
        Deposit money into an account.
        
        Args:
            account_number (str): Account number
            amount (float): Amount to deposit
            
        Returns:
            Transaction: The transaction object or None if account not found
        """
        account = self.get_account(account_number)
        if account:
            transaction_id = self.generate_transaction_id()
            transaction = account.deposit(amount, transaction_id)
            self.save_data()
            return transaction
        return None
    
    def withdraw(self, account_number, amount):
        """
        Withdraw money from an account.
        
        Args:
            account_number (str): Account number
            amount (float): Amount to withdraw
            
        Returns:
            Transaction: The transaction object or None if account not found
        """
        account = self.get_account(account_number)
        if account:
            transaction_id = self.generate_transaction_id()
            transaction = account.withdraw(amount, transaction_id)
            self.save_data()
            return transaction
        return None
    
    def check_balance(self, account_number):
        """
        Check account balance.
        
        Args:
            account_number (str): Account number
            
        Returns:
            float: Account balance or None if account not found
        """
        account = self.get_account(account_number)
        if account:
            return account.get_balance()
        return None
    
    def get_transaction_history(self, account_number, limit=None):
        """
        Get transaction history for an account.
        
        Args:
            account_number (str): Account number
            limit (int, optional): Maximum number of recent transactions to return
            
        Returns:
            list: List of transactions or None if account not found
        """
        account = self.get_account(account_number)
        if account:
            return account.get_transaction_history(limit)
        return None
    
    def save_data(self):
        """Save all data to file."""
        data = {
            'next_customer_id': self.next_customer_id,
            'next_account_number': self.next_account_number,
            'next_transaction_id': self.next_transaction_id,
            'customers': {cid: c.to_dict() for cid, c in self.customers.items()},
            'accounts': {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        }
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        """Load data from file if it exists."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                
                self.next_customer_id = data.get('next_customer_id', 1)
                self.next_account_number = data.get('next_account_number', 1000)
                self.next_transaction_id = data.get('next_transaction_id', 1)
                
                customers_data = data.get('customers', {})
                self.customers = {cid: Customer.from_dict(c) for cid, c in customers_data.items()}
                
                accounts_data = data.get('accounts', {})
                self.accounts = {acc_num: Account.from_dict(acc) for acc_num, acc in accounts_data.items()}
            except Exception as e:
                print(f"Error loading data: {e}")
                print("Starting with fresh data...")
