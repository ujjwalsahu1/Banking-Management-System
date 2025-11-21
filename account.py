"""Account module for banking management system."""

from datetime import datetime
from typing import List, Dict


class Account:
    """Represents a bank account with basic operations."""
    
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0):
        """Initialize a new account.
        
        Args:
            account_number: Unique account identifier
            customer_name: Name of the account holder
            initial_balance: Starting balance (default: 0.0)
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions: List[Dict] = []
        self.created_at = datetime.now()
        
        if initial_balance > 0:
            self._add_transaction("Initial Deposit", initial_balance)
    
    def deposit(self, amount: float) -> bool:
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive")
            return False
        
        self.balance += amount
        self._add_transaction("Deposit", amount)
        print(f"Successfully deposited ${amount:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient funds. Current balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        self._add_transaction("Withdrawal", -amount)
        print(f"Successfully withdrew ${amount:.2f}")
        return True
    
    def get_balance(self) -> float:
        """Get current account balance.
        
        Returns:
            Current balance
        """
        return self.balance
    
    def get_transactions(self) -> List[Dict]:
        """Get transaction history.
        
        Returns:
            List of transaction records
        """
        return self.transactions.copy()
    
    def _add_transaction(self, transaction_type: str, amount: float):
        """Add a transaction to the history.
        
        Args:
            transaction_type: Type of transaction
            amount: Transaction amount
        """
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.balance,
            'timestamp': datetime.now()
        }
        self.transactions.append(transaction)
    
    def display_account_info(self):
        """Display account information."""
        print("\n" + "="*50)
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Account Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
    
    def display_transactions(self):
        """Display transaction history."""
        if not self.transactions:
            print("\nNo transactions found.")
            return
        
        print("\n" + "="*70)
        print("TRANSACTION HISTORY")
        print("="*70)
        print(f"{'Type':<20} {'Amount':<15} {'Balance':<15} {'Date & Time'}")
        print("-"*70)
        
        for trans in self.transactions:
            amount_str = f"${abs(trans['amount']):.2f}"
            if trans['amount'] < 0:
                amount_str = f"-{amount_str}"
            
            balance_str = f"${trans['balance_after']:.2f}"
            
            print(f"{trans['type']:<20} {amount_str:<15} "
                  f"{balance_str:<15} "
                  f"{trans['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"Account({self.account_number}, {self.customer_name}, ${self.balance:.2f})"
    
    def __repr__(self) -> str:
        """Object representation of the account."""
        return self.__str__()
