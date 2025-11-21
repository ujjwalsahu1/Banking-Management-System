# Banking-Management-System

A simple and efficient application for managing core banking operations. It allows users to create accounts, manage customer details, perform deposits and withdrawals, check balances, and track transactions. The system is built with a clean, modular codebase, making it easy to extend and integrate with databases or additional features.

## Features

- **Account Management**: Create and delete bank accounts
- **Customer Management**: Create customers and manage their personal information
- **Deposits**: Deposit money into accounts
- **Withdrawals**: Withdraw money with balance validation
- **Balance Inquiry**: Check account balances
- **Transaction History**: Track all account transactions with timestamps
- **Account Details**: View comprehensive account information
- **Customer Details**: View and update customer information
- **Bank Summary**: View overall bank statistics
- **List Management**: List all accounts and customers

## Project Structure

```
Banking-Management-System/
├── account.py              # Account class with deposit/withdraw operations
├── customer.py             # Customer class for managing customer details
├── bank.py                 # Bank class for managing accounts and customers
├── main.py                 # Main application with CLI interface
├── test_banking_system.py  # Comprehensive unit tests
├── requirements.txt        # Project dependencies (none required)
└── README.md              # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ujjwalsahu1/Banking-Management-System.git
cd Banking-Management-System
```

2. No additional dependencies are required! The system uses only Python standard library.

## Usage

### Running the Application

```bash
python main.py
```

### Main Menu Options

```
1. Create New Account       - Create a new bank account
2. Create New Customer      - Create a new customer profile
3. Deposit Money           - Deposit funds into an account
4. Withdraw Money          - Withdraw funds from an account
5. Check Balance           - View current account balance
6. View Account Details    - View detailed account information
7. View Transaction History - View all transactions for an account
8. View Customer Details   - View customer information
9. Update Customer Information - Update customer email/phone/address
10. List All Accounts      - Display all accounts in the bank
11. List All Customers     - Display all customers
12. Bank Summary           - View overall bank statistics
13. Delete Account         - Delete an account (must have zero balance)
0. Exit                    - Exit the application
```

### Example Usage

```python
# Import the required modules
from bank import Bank
from account import Account

# Create a bank instance
bank = Bank("MyBank")

# Create an account
account = bank.create_account("John Doe", 1000.0)

# Perform operations
account.deposit(500.0)
account.withdraw(200.0)
print(f"Balance: ${account.get_balance():.2f}")

# View transaction history
account.display_transactions()
```

## Running Tests

Run the comprehensive test suite:

```bash
python test_banking_system.py
```

Or run with verbose output:

```bash
python test_banking_system.py -v
```

## Code Examples

### Creating a Customer

```python
from bank import Bank

bank = Bank("MyBank")
customer = bank.create_customer(
    name="John Doe",
    email="john@example.com",
    phone="1234567890",
    address="123 Main St"
)
```

### Managing Accounts

```python
# Create an account
account = bank.create_account("Jane Doe", 5000.0)

# Deposit money
account.deposit(1000.0)

# Withdraw money
account.withdraw(500.0)

# Check balance
balance = account.get_balance()
print(f"Current Balance: ${balance:.2f}")
```

### Viewing Transaction History

```python
# Display all transactions
account.display_transactions()

# Get transactions as a list
transactions = account.get_transactions()
for trans in transactions:
    print(f"{trans['type']}: ${trans['amount']:.2f}")
```

## Features Explained

### Account Class
- Automatic transaction tracking with timestamps
- Balance validation for withdrawals
- Initial balance support
- Transaction history display

### Customer Class
- Store customer personal information
- Update email, phone, and address
- Display customer details

### Bank Class
- Manage multiple accounts and customers
- Auto-increment account numbers and customer IDs
- Calculate total deposits
- List all accounts and customers
- Delete accounts with zero balance

## Security Features

- Input validation for all operations
- Prevents negative deposits and withdrawals
- Prevents overdrafts (insufficient funds)
- Prevents deletion of accounts with balance
- Validates initial account balance

## Future Enhancements

- Database integration (SQLite, PostgreSQL, MySQL)
- User authentication and authorization
- Interest calculation
- Account types (Savings, Checking, etc.)
- Transfer between accounts
- Transaction categories and notes
- Export reports (PDF, CSV)
- Web interface
- REST API

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

ujjwalsahu1

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
