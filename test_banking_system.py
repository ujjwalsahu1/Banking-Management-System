"""Unit tests for the Banking Management System."""

import unittest
from datetime import datetime
from account import Account
from customer import Customer
from bank import Bank


class TestAccount(unittest.TestCase):
    """Test cases for Account class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.account = Account("ACC000001", "John Doe", 1000.0)
    
    def test_account_creation(self):
        """Test account creation."""
        self.assertEqual(self.account.account_number, "ACC000001")
        self.assertEqual(self.account.customer_name, "John Doe")
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(len(self.account.transactions), 1)
    
    def test_account_creation_with_zero_balance(self):
        """Test account creation with zero balance."""
        account = Account("ACC000002", "Jane Doe", 0.0)
        self.assertEqual(account.balance, 0.0)
        self.assertEqual(len(account.transactions), 0)
    
    def test_account_creation_negative_balance(self):
        """Test account creation with negative balance raises error."""
        with self.assertRaises(ValueError):
            Account("ACC000003", "Bob Smith", -100.0)
    
    def test_deposit_success(self):
        """Test successful deposit."""
        initial_balance = self.account.balance
        result = self.account.deposit(500.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, initial_balance + 500.0)
        self.assertEqual(len(self.account.transactions), 2)
    
    def test_deposit_negative_amount(self):
        """Test deposit with negative amount fails."""
        initial_balance = self.account.balance
        result = self.account.deposit(-100.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, initial_balance)
    
    def test_deposit_zero_amount(self):
        """Test deposit with zero amount fails."""
        initial_balance = self.account.balance
        result = self.account.deposit(0.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, initial_balance)
    
    def test_withdraw_success(self):
        """Test successful withdrawal."""
        initial_balance = self.account.balance
        result = self.account.withdraw(300.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, initial_balance - 300.0)
        self.assertEqual(len(self.account.transactions), 2)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds fails."""
        initial_balance = self.account.balance
        result = self.account.withdraw(2000.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, initial_balance)
    
    def test_withdraw_negative_amount(self):
        """Test withdrawal with negative amount fails."""
        initial_balance = self.account.balance
        result = self.account.withdraw(-100.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, initial_balance)
    
    def test_withdraw_zero_amount(self):
        """Test withdrawal with zero amount fails."""
        initial_balance = self.account.balance
        result = self.account.withdraw(0.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, initial_balance)
    
    def test_get_balance(self):
        """Test get balance."""
        self.assertEqual(self.account.get_balance(), 1000.0)
        self.account.deposit(500.0)
        self.assertEqual(self.account.get_balance(), 1500.0)
    
    def test_get_transactions(self):
        """Test get transactions."""
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['type'], 'Initial Deposit')
        
        self.account.deposit(200.0)
        self.account.withdraw(100.0)
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 3)
    
    def test_transaction_history(self):
        """Test transaction history tracking."""
        self.account.deposit(500.0)
        self.account.withdraw(200.0)
        
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 3)
        self.assertEqual(transactions[1]['type'], 'Deposit')
        self.assertEqual(transactions[1]['amount'], 500.0)
        self.assertEqual(transactions[2]['type'], 'Withdrawal')
        self.assertEqual(transactions[2]['amount'], -200.0)


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.customer = Customer("CUST0001", "John Doe", "john@example.com", "1234567890", "123 Main St")
    
    def test_customer_creation(self):
        """Test customer creation."""
        self.assertEqual(self.customer.customer_id, "CUST0001")
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john@example.com")
        self.assertEqual(self.customer.phone, "1234567890")
        self.assertEqual(self.customer.address, "123 Main St")
    
    def test_customer_creation_without_address(self):
        """Test customer creation without address."""
        customer = Customer("CUST0002", "Jane Doe", "jane@example.com", "0987654321")
        self.assertEqual(customer.address, "")
    
    def test_update_email(self):
        """Test updating email."""
        new_email = "newemail@example.com"
        self.customer.update_email(new_email)
        self.assertEqual(self.customer.email, new_email)
    
    def test_update_phone(self):
        """Test updating phone."""
        new_phone = "5555555555"
        self.customer.update_phone(new_phone)
        self.assertEqual(self.customer.phone, new_phone)
    
    def test_update_address(self):
        """Test updating address."""
        new_address = "456 Oak Ave"
        self.customer.update_address(new_address)
        self.assertEqual(self.customer.address, new_address)


class TestBank(unittest.TestCase):
    """Test cases for Bank class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.bank = Bank("Test Bank")
    
    def test_bank_creation(self):
        """Test bank creation."""
        self.assertEqual(self.bank.bank_name, "Test Bank")
        self.assertEqual(len(self.bank.accounts), 0)
        self.assertEqual(len(self.bank.customers), 0)
    
    def test_create_customer(self):
        """Test creating a customer."""
        customer = self.bank.create_customer("John Doe", "john@example.com", "1234567890", "123 Main St")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.customer_id, "CUST0001")
        self.assertEqual(len(self.bank.customers), 1)
    
    def test_create_multiple_customers(self):
        """Test creating multiple customers."""
        customer1 = self.bank.create_customer("John Doe", "john@example.com", "1234567890")
        customer2 = self.bank.create_customer("Jane Doe", "jane@example.com", "0987654321")
        
        self.assertEqual(len(self.bank.customers), 2)
        self.assertEqual(customer1.customer_id, "CUST0001")
        self.assertEqual(customer2.customer_id, "CUST0002")
    
    def test_create_account(self):
        """Test creating an account."""
        account = self.bank.create_account("John Doe", 1000.0)
        self.assertIsNotNone(account)
        self.assertEqual(account.account_number, "ACC001000")
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(len(self.bank.accounts), 1)
    
    def test_create_multiple_accounts(self):
        """Test creating multiple accounts."""
        account1 = self.bank.create_account("John Doe", 1000.0)
        account2 = self.bank.create_account("Jane Doe", 2000.0)
        
        self.assertEqual(len(self.bank.accounts), 2)
        self.assertEqual(account1.account_number, "ACC001000")
        self.assertEqual(account2.account_number, "ACC001001")
    
    def test_create_account_with_negative_balance(self):
        """Test creating account with negative balance fails."""
        account = self.bank.create_account("Bob Smith", -500.0)
        self.assertIsNone(account)
        self.assertEqual(len(self.bank.accounts), 0)
    
    def test_get_account(self):
        """Test getting an account."""
        created_account = self.bank.create_account("John Doe", 1000.0)
        retrieved_account = self.bank.get_account(created_account.account_number)
        
        self.assertEqual(created_account, retrieved_account)
    
    def test_get_nonexistent_account(self):
        """Test getting a nonexistent account."""
        account = self.bank.get_account("ACC999999")
        self.assertIsNone(account)
    
    def test_get_customer(self):
        """Test getting a customer."""
        created_customer = self.bank.create_customer("John Doe", "john@example.com", "1234567890")
        retrieved_customer = self.bank.get_customer(created_customer.customer_id)
        
        self.assertEqual(created_customer, retrieved_customer)
    
    def test_get_nonexistent_customer(self):
        """Test getting a nonexistent customer."""
        customer = self.bank.get_customer("CUST9999")
        self.assertIsNone(customer)
    
    def test_delete_account(self):
        """Test deleting an account."""
        account = self.bank.create_account("John Doe", 0.0)
        result = self.bank.delete_account(account.account_number)
        
        self.assertTrue(result)
        self.assertEqual(len(self.bank.accounts), 0)
    
    def test_delete_account_with_balance(self):
        """Test deleting account with balance fails."""
        account = self.bank.create_account("John Doe", 1000.0)
        result = self.bank.delete_account(account.account_number)
        
        self.assertFalse(result)
        self.assertEqual(len(self.bank.accounts), 1)
    
    def test_delete_nonexistent_account(self):
        """Test deleting nonexistent account fails."""
        result = self.bank.delete_account("ACC999999")
        self.assertFalse(result)
    
    def test_get_total_deposits(self):
        """Test calculating total deposits."""
        self.bank.create_account("John Doe", 1000.0)
        self.bank.create_account("Jane Doe", 2000.0)
        self.bank.create_account("Bob Smith", 1500.0)
        
        total = self.bank.get_total_deposits()
        self.assertEqual(total, 4500.0)
    
    def test_get_total_deposits_empty_bank(self):
        """Test total deposits for empty bank."""
        total = self.bank.get_total_deposits()
        self.assertEqual(total, 0.0)


if __name__ == '__main__':
    unittest.main()
