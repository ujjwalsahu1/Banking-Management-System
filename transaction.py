"""Transaction class for tracking all banking transactions."""

from datetime import datetime

class Transaction:
    """Represents a banking transaction."""
    
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"
    
    def __init__(self, transaction_id, account_number, transaction_type, amount, balance_after, timestamp=None):
        """
        Initialize a new transaction.
        
        Args:
            transaction_id (str): Unique transaction identifier
            account_number (str): Account number associated with transaction
            transaction_type (str): Type of transaction (DEPOSIT, WITHDRAWAL, TRANSFER)
            amount (float): Transaction amount
            balance_after (float): Account balance after transaction
            timestamp (str, optional): Transaction timestamp
        """
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = timestamp if timestamp else datetime.now().isoformat()
    
    def to_dict(self):
        """Convert transaction to dictionary for storage."""
        return {
            'transaction_id': self.transaction_id,
            'account_number': self.account_number,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'balance_after': self.balance_after,
            'timestamp': self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create transaction from dictionary."""
        return cls(
            data['transaction_id'],
            data['account_number'],
            data['transaction_type'],
            data['amount'],
            data['balance_after'],
            data['timestamp']
        )
    
    def __str__(self):
        """String representation of transaction."""
        return f"{self.timestamp} | {self.transaction_type} | Amount: ${self.amount:.2f} | Balance: ${self.balance_after:.2f}"
