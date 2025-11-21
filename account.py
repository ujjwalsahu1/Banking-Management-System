"""Account class for managing bank accounts."""

from transaction import Transaction

class Account:
    """Represents a bank account."""
    
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"
    
    def __init__(self, account_number, customer_id, account_type, balance=0.0):
        """
        Initialize a new account.
        
        Args:
            account_number (str): Unique account number
            customer_id (str): ID of the customer who owns the account
            account_type (str): Type of account (CHECKING or SAVINGS)
            balance (float, optional): Initial balance, defaults to 0.0
        """
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount, transaction_id):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            transaction_id (str): Unique transaction identifier
            
        Returns:
            Transaction: The transaction object
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        transaction = Transaction(
            transaction_id,
            self.account_number,
            Transaction.DEPOSIT,
            amount,
            self.balance
        )
        self.transactions.append(transaction)
        return transaction
    
    def withdraw(self, amount, transaction_id):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            transaction_id (str): Unique transaction identifier
            
        Returns:
            Transaction: The transaction object
            
        Raises:
            ValueError: If amount is not positive or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        transaction = Transaction(
            transaction_id,
            self.account_number,
            Transaction.WITHDRAWAL,
            amount,
            self.balance
        )
        self.transactions.append(transaction)
        return transaction
    
    def get_balance(self):
        """Get current account balance."""
        return self.balance
    
    def get_transaction_history(self, limit=None):
        """
        Get transaction history.
        
        Args:
            limit (int, optional): Maximum number of recent transactions to return
            
        Returns:
            list: List of transactions
        """
        if limit:
            return self.transactions[-limit:]
        return self.transactions
    
    def to_dict(self):
        """Convert account to dictionary for storage."""
        return {
            'account_number': self.account_number,
            'customer_id': self.customer_id,
            'account_type': self.account_type,
            'balance': self.balance,
            'transactions': [t.to_dict() for t in self.transactions]
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create account from dictionary."""
        account = cls(
            data['account_number'],
            data['customer_id'],
            data['account_type'],
            data['balance']
        )
        account.transactions = [Transaction.from_dict(t) for t in data.get('transactions', [])]
        return account
    
    def __str__(self):
        """String representation of account."""
        return f"Account Number: {self.account_number}\nType: {self.account_type}\nBalance: ${self.balance:.2f}"
