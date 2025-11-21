# Banking Management System

A simple and efficient application for managing core banking operations. It allows users to create accounts, manage customer details, perform deposits and withdrawals, check balances, and track transactions. The system is built with a clean, modular codebase, making it easy to extend and integrate with databases or additional features.

## Features

- **Customer Management**: Create, view, update, and list customer information
- **Account Management**: Create checking and savings accounts with initial deposits
- **Banking Operations**: 
  - Deposit money into accounts
  - Withdraw money from accounts
  - Check account balances
- **Transaction Tracking**: Complete history of all transactions with timestamps
- **Data Persistence**: Automatic saving and loading of data using JSON file storage
- **Error Handling**: Validates inputs and prevents invalid operations (e.g., insufficient funds)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ujjwalsahu1/Banking-Management-System.git
cd Banking-Management-System
```

2. No additional installation required! The system uses only Python standard library.

## Usage

### Running the Application

Start the banking system with:
```bash
python3 main.py
```

### Main Menu Options

1. **Customer Management**
   - Create new customers
   - View customer details
   - Update customer information
   - List all customers

2. **Account Management**
   - Create new accounts (Checking or Savings)
   - View account details
   - View all accounts for a customer

3. **Deposit Money**
   - Deposit funds into any account

4. **Withdraw Money**
   - Withdraw funds from any account (with balance validation)

5. **Check Balance**
   - View current account balance

6. **Transaction History**
   - View complete or recent transaction history for an account

### Example Workflow

```bash
# 1. Start the application
python3 main.py

# 2. Create a customer (Option 1 -> 1)
#    - Enter name, email, phone, address
#    - System generates Customer ID (e.g., CUST000001)

# 3. Create an account (Option 2 -> 1)
#    - Enter Customer ID
#    - Select account type (Checking/Savings)
#    - Enter initial deposit
#    - System generates Account Number (e.g., ACC00001000)

# 4. Perform transactions (Options 3-6)
#    - Use the Account Number for all operations
```

## Project Structure

```
Banking-Management-System/
├── customer.py          # Customer class and management
├── account.py           # Account class with deposit/withdrawal logic
├── transaction.py       # Transaction tracking class
├── banking_system.py    # Main banking system logic and data persistence
├── main.py             # CLI application interface
├── requirements.txt    # Python dependencies (none required)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Code Example

```python
from banking_system import BankingSystem
from account import Account

# Initialize the banking system
bank = BankingSystem()

# Create a customer
customer = bank.create_customer('John Doe', 'john@example.com', '555-1234', '123 Main St')
print(f"Customer ID: {customer.customer_id}")

# Create a checking account with initial deposit
account = bank.create_account(customer.customer_id, Account.CHECKING, 1000.0)
print(f"Account Number: {account.account_number}")

# Deposit money
transaction = bank.deposit(account.account_number, 500.0)
print(f"New balance: ${account.balance:.2f}")

# Withdraw money
transaction = bank.withdraw(account.account_number, 200.0)
print(f"New balance: ${account.balance:.2f}")

# Check balance
balance = bank.check_balance(account.account_number)
print(f"Current balance: ${balance:.2f}")

# Get transaction history
transactions = bank.get_transaction_history(account.account_number)
for txn in transactions:
    print(txn)
```

## Data Storage

The system automatically saves all data to `banking_data.json` in the current directory. This file contains:
- All customer information
- All account details
- Complete transaction history
- System counters (customer IDs, account numbers, transaction IDs)

The data is automatically loaded when the application starts, ensuring persistence across sessions.

## Error Handling

The system includes comprehensive error handling:
- Prevents negative deposits or withdrawals
- Validates sufficient funds before withdrawals
- Checks for valid customer IDs and account numbers
- Handles file I/O errors gracefully

## Future Enhancements

Potential features for future versions:
- Transfer money between accounts
- Interest calculation for savings accounts
- Account statements and reports
- Multi-user authentication
- Database integration (PostgreSQL, MySQL)
- Web-based interface
- Mobile app integration

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
