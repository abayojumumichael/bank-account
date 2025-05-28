# Bank Account Python Project

This project provides a simple `BankAccount` class in Python to simulate basic banking operations such as deposit, withdrawal, balance inquiry, and updating the account holder's name.

## Features
- Create a bank account with an account holder's name
- Deposit money into the account
- Withdraw money from the account (with balance check)
- Show current account balance
- Update the account holder's name
- String representation of the account for easy display

## Usage

1. **Import or use the `BankAccount` class:**

```python
from bankaccount import BankAccount

# Create an account
account = BankAccount("Amari")

# Show balance
account.show_balance()

# Deposit money
account.deposit(100)

# Withdraw money
account.withdraw(50)

# Update account holder's name
account.update_name("Bola")

# Print account details
print(account)
```

2. **Error Handling:**
- Creating an account without a name raises a `ValueError`.
- Depositing zero or negative amounts is not allowed.
- Withdrawing more than the available balance is not allowed.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.