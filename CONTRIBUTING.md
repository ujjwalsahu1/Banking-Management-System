# Contributing to Banking Management System

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Banking-Management-System.git
   cd Banking-Management-System
   ```
3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Requirements
- Python 3.6 or higher
- No external dependencies required

### Running Tests
```bash
python test_banking_system.py -v
```

All tests must pass before submitting a pull request.

## Code Style Guidelines

### Python Style
- Follow PEP 8 guidelines
- Use descriptive variable and function names
- Add docstrings to all classes and methods
- Keep functions focused and small

### Example
```python
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
    return True
```

## Testing Guidelines

### Writing Tests
- Add tests for all new features
- Test both success and failure cases
- Use descriptive test names
- Follow the existing test structure

### Example Test
```python
def test_deposit_success(self):
    """Test successful deposit."""
    initial_balance = self.account.balance
    result = self.account.deposit(500.0)
    self.assertTrue(result)
    self.assertEqual(self.account.balance, initial_balance + 500.0)
```

## Contribution Areas

### Features to Implement
- [ ] Database integration (SQLite)
- [ ] Interest calculation for savings accounts
- [ ] Account types (Checking, Savings, etc.)
- [ ] Transfer between accounts
- [ ] Transaction categories
- [ ] Export reports (PDF, CSV)
- [ ] Web interface using Flask/Django
- [ ] REST API
- [ ] Authentication and authorization
- [ ] Multi-currency support

### Bug Fixes
- Check the Issues page for known bugs
- Create an issue before starting work
- Reference the issue number in your commit

### Documentation
- Improve README
- Add code examples
- Improve docstrings
- Add tutorials

## Pull Request Process

1. **Update tests**
   - Add tests for new functionality
   - Ensure all tests pass

2. **Update documentation**
   - Update README if needed
   - Update USAGE_GUIDE if needed
   - Add docstrings to new code

3. **Create Pull Request**
   - Use a descriptive title
   - Describe what changes you made
   - Reference any related issues
   - Request review

4. **Code Review**
   - Address review comments
   - Update code as needed
   - Request re-review

## Commit Message Guidelines

### Format
```
type: brief description

Detailed description if needed

Fixes #issue_number
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Maintenance tasks

### Examples
```
feat: add interest calculation for savings accounts

Add method to calculate and apply interest to savings accounts
based on annual percentage rate.

Fixes #123
```

```
fix: prevent negative withdrawal amounts

Add validation to ensure withdrawal amounts are positive.
Display error message for invalid amounts.

Fixes #456
```

## Code Review Checklist

Before submitting, verify:
- [ ] Code follows style guidelines
- [ ] Tests are added and passing
- [ ] Documentation is updated
- [ ] No debugging code left
- [ ] No unused imports
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

## Questions or Issues?

- Open an issue for bug reports
- Open an issue for feature requests
- Use discussions for questions
- Contact maintainers for urgent matters

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

## Thank You!

Your contributions help make this project better for everyone. We appreciate your time and effort!
