# Banking Management System - Usage Guide

## Quick Start

### 1. Running the Application

```bash
python main.py
```

### 2. Creating Your First Account

When the menu appears:
1. Select option `1` (Create New Account)
2. Enter customer name: `John Doe`
3. Enter initial balance: `1000`
4. Note the account number displayed (e.g., `ACC001000`)

### 3. Making a Deposit

1. Select option `3` (Deposit Money)
2. Enter the account number
3. Enter the amount to deposit
4. Confirmation will be displayed

### 4. Making a Withdrawal

1. Select option `4` (Withdraw Money)
2. Enter the account number
3. Enter the amount to withdraw
4. Confirmation will be displayed (or error if insufficient funds)

### 5. Checking Balance

1. Select option `5` (Check Balance)
2. Enter the account number
3. Current balance will be displayed

## Complete Feature Walkthrough

### Account Operations

#### Create Account
```
Menu Option: 1
Input: Customer Name, Initial Balance
Output: Account Number (auto-generated)
```

#### View Account Details
```
Menu Option: 6
Input: Account Number
Output: Account information, balance, creation date
```

#### Delete Account
```
Menu Option: 13
Input: Account Number
Requirement: Account balance must be $0.00
Output: Confirmation of deletion
```

### Customer Operations

#### Create Customer
```
Menu Option: 2
Input: Name, Email, Phone, Address (optional)
Output: Customer ID (auto-generated)
```

#### View Customer Details
```
Menu Option: 8
Input: Customer ID
Output: Customer information
```

#### Update Customer Information
```
Menu Option: 9
Input: Customer ID
Then select what to update:
  1. Email
  2. Phone
  3. Address
Output: Confirmation of update
```

### Transaction Operations

#### Deposit
```
Menu Option: 3
Input: Account Number, Amount
Validation: Amount must be > 0
Output: Success message with new balance
```

#### Withdraw
```
Menu Option: 4
Input: Account Number, Amount
Validation: 
  - Amount must be > 0
  - Amount must be ≤ current balance
Output: Success message with new balance
```

#### Check Balance
```
Menu Option: 5
Input: Account Number
Output: Account number, customer name, current balance
```

#### View Transaction History
```
Menu Option: 7
Input: Account Number
Output: Complete transaction history with timestamps
```

### Reporting Operations

#### List All Accounts
```
Menu Option: 10
Output: Table of all accounts with balances and transaction counts
```

#### List All Customers
```
Menu Option: 11
Output: Table of all customers with contact information
```

#### Bank Summary
```
Menu Option: 12
Output: 
  - Total number of accounts
  - Total number of customers
  - Total deposits across all accounts
```

## Error Handling

### Common Errors and Solutions

#### "Account not found"
- **Cause**: Invalid or non-existent account number
- **Solution**: Verify the account number using option 10 (List All Accounts)

#### "Insufficient funds"
- **Cause**: Withdrawal amount exceeds current balance
- **Solution**: Check balance first (option 5), then withdraw available amount

#### "Deposit/Withdrawal amount must be positive"
- **Cause**: Zero or negative amount entered
- **Solution**: Enter a positive number

#### "Cannot delete account with non-zero balance"
- **Cause**: Attempting to delete an account that has money
- **Solution**: Withdraw all funds first, then delete

#### "Initial balance cannot be negative"
- **Cause**: Negative value entered when creating account
- **Solution**: Enter zero or positive value

## Tips and Best Practices

### For Users

1. **Keep Track of Account Numbers**: Write down account numbers when created
2. **Check Balance Before Withdrawal**: Always verify sufficient funds
3. **Review Transaction History**: Regularly check transactions for accuracy
4. **Update Customer Information**: Keep contact details current

### For Developers

1. **Input Validation**: All user inputs are validated
2. **Error Messages**: Clear, informative error messages
3. **Transaction Tracking**: Every operation is logged with timestamp
4. **Data Integrity**: Account balances are protected from invalid operations

## Sample Workflow

Here's a typical workflow for managing a customer:

```
Step 1: Create Customer
- Menu: 2
- Input: John Doe, john@email.com, 555-1234, 123 Main St

Step 2: Create Account for Customer
- Menu: 1
- Input: John Doe, 5000.00
- Output: ACC001000

Step 3: Make Deposit
- Menu: 3
- Input: ACC001000, 1000.00

Step 4: Make Withdrawal
- Menu: 4
- Input: ACC001000, 500.00

Step 5: View Transaction History
- Menu: 7
- Input: ACC001000

Step 6: Check Balance
- Menu: 5
- Input: ACC001000
- Output: $5500.00
```

## Advanced Usage

### Programmatic Access

You can use the banking system components in your own Python code:

```python
from bank import Bank

# Create a bank
bank = Bank("MyBank")

# Create customer
customer = bank.create_customer("John Doe", "john@email.com", "555-1234")

# Create account
account = bank.create_account("John Doe", 1000.0)

# Perform transactions
account.deposit(500.0)
account.withdraw(200.0)

# Get balance
balance = account.get_balance()

# View transactions
transactions = account.get_transactions()
```

### Running Tests

```bash
# Run all tests
python test_banking_system.py

# Run with verbose output
python test_banking_system.py -v

# Run specific test
python test_banking_system.py TestAccount.test_deposit_success
```

### Running Demo

```bash
# Run the demonstration script
python demo.py
```

This will showcase all features of the system with sample data.

## Troubleshooting

### Issue: Program exits immediately
- **Solution**: Check Python version (requires Python 3.6+)

### Issue: Import errors
- **Solution**: Ensure all files are in the same directory

### Issue: Cannot enter input
- **Solution**: Make sure terminal is interactive (not redirected)

## Support

For additional help or to report issues, please refer to the README.md file or contact the repository maintainer.
