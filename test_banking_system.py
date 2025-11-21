"""Unit tests for the Banking Management System."""

import unittest
import os
from customer import Customer
from account import Account
from transaction import Transaction
from banking_system import BankingSystem


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""
    
    def test_customer_creation(self):
        """Test creating a customer."""
        customer = Customer("CUST001", "John Doe", "john@example.com", "555-1234", "123 Main St")
        self.assertEqual(customer.customer_id, "CUST001")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
    
    def test_customer_update(self):
        """Test updating customer details."""
        customer = Customer("CUST001", "John Doe", "john@example.com", "555-1234", "123 Main St")
        customer.update_details(name="Jane Doe", email="jane@example.com")
        self.assertEqual(customer.name, "Jane Doe")
        self.assertEqual(customer.email, "jane@example.com")
        self.assertEqual(customer.phone, "555-1234")  # Should remain unchanged
    
    def test_customer_to_dict(self):
        """Test converting customer to dictionary."""
        customer = Customer("CUST001", "John Doe", "john@example.com", "555-1234", "123 Main St")
        data = customer.to_dict()
        self.assertEqual(data['customer_id'], "CUST001")
        self.assertEqual(data['name'], "John Doe")
    
    def test_customer_from_dict(self):
        """Test creating customer from dictionary."""
        data = {
            'customer_id': "CUST001",
            'name': "John Doe",
            'email': "john@example.com",
            'phone': "555-1234",
            'address': "123 Main St"
        }
        customer = Customer.from_dict(data)
        self.assertEqual(customer.customer_id, "CUST001")
        self.assertEqual(customer.name, "John Doe")


class TestAccount(unittest.TestCase):
    """Test cases for Account class."""
    
    def test_account_creation(self):
        """Test creating an account."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        self.assertEqual(account.account_number, "ACC001")
        self.assertEqual(account.customer_id, "CUST001")
        self.assertEqual(account.balance, 1000.0)
    
    def test_deposit(self):
        """Test depositing money."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        transaction = account.deposit(500.0, "TXN001")
        self.assertEqual(account.balance, 1500.0)
        self.assertEqual(transaction.amount, 500.0)
        self.assertEqual(transaction.transaction_type, Transaction.DEPOSIT)
    
    def test_deposit_negative_amount(self):
        """Test depositing negative amount raises error."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        with self.assertRaises(ValueError):
            account.deposit(-100.0, "TXN001")
    
    def test_withdraw(self):
        """Test withdrawing money."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        transaction = account.withdraw(300.0, "TXN001")
        self.assertEqual(account.balance, 700.0)
        self.assertEqual(transaction.amount, 300.0)
        self.assertEqual(transaction.transaction_type, Transaction.WITHDRAWAL)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than balance raises error."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(200.0, "TXN001")
    
    def test_withdraw_negative_amount(self):
        """Test withdrawing negative amount raises error."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        with self.assertRaises(ValueError):
            account.withdraw(-100.0, "TXN001")
    
    def test_get_balance(self):
        """Test getting account balance."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        self.assertEqual(account.get_balance(), 1000.0)
    
    def test_transaction_history(self):
        """Test getting transaction history."""
        account = Account("ACC001", "CUST001", Account.CHECKING, 1000.0)
        account.deposit(500.0, "TXN001")
        account.withdraw(200.0, "TXN002")
        
        history = account.get_transaction_history()
        self.assertEqual(len(history), 2)
        
        limited_history = account.get_transaction_history(limit=1)
        self.assertEqual(len(limited_history), 1)


class TestTransaction(unittest.TestCase):
    """Test cases for Transaction class."""
    
    def test_transaction_creation(self):
        """Test creating a transaction."""
        transaction = Transaction("TXN001", "ACC001", Transaction.DEPOSIT, 500.0, 1500.0)
        self.assertEqual(transaction.transaction_id, "TXN001")
        self.assertEqual(transaction.account_number, "ACC001")
        self.assertEqual(transaction.amount, 500.0)
    
    def test_transaction_to_dict(self):
        """Test converting transaction to dictionary."""
        transaction = Transaction("TXN001", "ACC001", Transaction.DEPOSIT, 500.0, 1500.0)
        data = transaction.to_dict()
        self.assertEqual(data['transaction_id'], "TXN001")
        self.assertEqual(data['amount'], 500.0)
    
    def test_transaction_from_dict(self):
        """Test creating transaction from dictionary."""
        data = {
            'transaction_id': "TXN001",
            'account_number': "ACC001",
            'transaction_type': Transaction.DEPOSIT,
            'amount': 500.0,
            'balance_after': 1500.0,
            'timestamp': "2025-01-01T12:00:00"
        }
        transaction = Transaction.from_dict(data)
        self.assertEqual(transaction.transaction_id, "TXN001")
        self.assertEqual(transaction.amount, 500.0)


class TestBankingSystem(unittest.TestCase):
    """Test cases for BankingSystem class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_file = "test_banking_data.json"
        self.bank = BankingSystem(self.test_file)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_create_customer(self):
        """Test creating a customer."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        self.assertIsNotNone(customer)
        self.assertTrue(customer.customer_id.startswith("CUST"))
        self.assertEqual(customer.name, "John Doe")
    
    def test_get_customer(self):
        """Test getting a customer."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        retrieved = self.bank.get_customer(customer.customer_id)
        self.assertEqual(retrieved.customer_id, customer.customer_id)
    
    def test_update_customer(self):
        """Test updating customer details."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        result = self.bank.update_customer(customer.customer_id, name="Jane Doe")
        self.assertTrue(result)
        updated = self.bank.get_customer(customer.customer_id)
        self.assertEqual(updated.name, "Jane Doe")
    
    def test_create_account(self):
        """Test creating an account."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        account = self.bank.create_account(customer.customer_id, Account.CHECKING, 1000.0)
        self.assertIsNotNone(account)
        self.assertTrue(account.account_number.startswith("ACC"))
        self.assertEqual(account.balance, 1000.0)  # Initial deposit should be counted once
    
    def test_create_account_invalid_customer(self):
        """Test creating account with invalid customer ID."""
        account = self.bank.create_account("INVALID", Account.CHECKING, 1000.0)
        self.assertIsNone(account)
    
    def test_deposit(self):
        """Test depositing money."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        account = self.bank.create_account(customer.customer_id, Account.CHECKING, 0.0)
        transaction = self.bank.deposit(account.account_number, 500.0)
        self.assertIsNotNone(transaction)
        self.assertEqual(account.balance, 500.0)
    
    def test_withdraw(self):
        """Test withdrawing money."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        account = self.bank.create_account(customer.customer_id, Account.CHECKING, 1000.0)
        transaction = self.bank.withdraw(account.account_number, 300.0)
        self.assertIsNotNone(transaction)
    
    def test_check_balance(self):
        """Test checking balance."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        account = self.bank.create_account(customer.customer_id, Account.CHECKING, 1000.0)
        balance = self.bank.check_balance(account.account_number)
        self.assertIsNotNone(balance)
    
    def test_get_transaction_history(self):
        """Test getting transaction history."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        account = self.bank.create_account(customer.customer_id, Account.CHECKING, 1000.0)
        self.bank.deposit(account.account_number, 500.0)
        self.bank.withdraw(account.account_number, 200.0)
        
        history = self.bank.get_transaction_history(account.account_number)
        self.assertIsNotNone(history)
        self.assertGreater(len(history), 0)
    
    def test_data_persistence(self):
        """Test data persistence across instances."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "555-1234", "123 Main St")
        account = self.bank.create_account(customer.customer_id, Account.CHECKING, 1000.0)
        
        # Create new instance with same file
        bank2 = BankingSystem(self.test_file)
        retrieved_customer = bank2.get_customer(customer.customer_id)
        retrieved_account = bank2.get_account(account.account_number)
        
        self.assertEqual(retrieved_customer.name, "John Doe")
        self.assertIsNotNone(retrieved_account)


if __name__ == '__main__':
    unittest.main()
