"""Main application for Banking Management System."""

from bank import Bank


class BankingApp:
    """Main banking application with CLI interface."""
    
    def __init__(self):
        """Initialize the banking application."""
        self.bank = Bank("MyBank")
        self.running = True
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("BANKING MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Create New Account")
        print("2. Create New Customer")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. View Account Details")
        print("7. View Transaction History")
        print("8. View Customer Details")
        print("9. Update Customer Information")
        print("10. List All Accounts")
        print("11. List All Customers")
        print("12. Bank Summary")
        print("13. Delete Account")
        print("0. Exit")
        print("="*50)
    
    def get_input(self, prompt: str, input_type=str):
        """Get and validate user input.
        
        Args:
            prompt: Input prompt to display
            input_type: Expected type (str, int, float)
            
        Returns:
            Validated input value
        """
        while True:
            try:
                value = input(prompt)
                if input_type == str:
                    return value.strip()
                elif input_type == int:
                    return int(value)
                elif input_type == float:
                    return float(value)
            except ValueError:
                print(f"Invalid input. Please enter a valid {input_type.__name__}.")
    
    def create_account(self):
        """Handle account creation."""
        print("\n--- Create New Account ---")
        customer_name = self.get_input("Enter customer name: ", str)
        
        if not customer_name:
            print("Error: Customer name cannot be empty")
            return
        
        initial_balance = self.get_input("Enter initial balance (or 0): $", float)
        self.bank.create_account(customer_name, initial_balance)
    
    def create_customer(self):
        """Handle customer creation."""
        print("\n--- Create New Customer ---")
        name = self.get_input("Enter customer name: ", str)
        email = self.get_input("Enter email: ", str)
        phone = self.get_input("Enter phone number: ", str)
        address = self.get_input("Enter address (optional): ", str)
        
        if not name or not email or not phone:
            print("Error: Name, email, and phone are required")
            return
        
        self.bank.create_customer(name, email, phone, address)
    
    def deposit_money(self):
        """Handle deposit operation."""
        print("\n--- Deposit Money ---")
        account_number = self.get_input("Enter account number: ", str)
        
        account = self.bank.get_account(account_number)
        if not account:
            print(f"Error: Account {account_number} not found")
            return
        
        amount = self.get_input("Enter amount to deposit: $", float)
        account.deposit(amount)
    
    def withdraw_money(self):
        """Handle withdrawal operation."""
        print("\n--- Withdraw Money ---")
        account_number = self.get_input("Enter account number: ", str)
        
        account = self.bank.get_account(account_number)
        if not account:
            print(f"Error: Account {account_number} not found")
            return
        
        amount = self.get_input("Enter amount to withdraw: $", float)
        account.withdraw(amount)
    
    def check_balance(self):
        """Handle balance inquiry."""
        print("\n--- Check Balance ---")
        account_number = self.get_input("Enter account number: ", str)
        
        account = self.bank.get_account(account_number)
        if not account:
            print(f"Error: Account {account_number} not found")
            return
        
        print(f"\nAccount: {account_number}")
        print(f"Customer: {account.customer_name}")
        print(f"Current Balance: ${account.get_balance():.2f}")
    
    def view_account_details(self):
        """Handle viewing account details."""
        print("\n--- View Account Details ---")
        account_number = self.get_input("Enter account number: ", str)
        
        account = self.bank.get_account(account_number)
        if not account:
            print(f"Error: Account {account_number} not found")
            return
        
        account.display_account_info()
    
    def view_transactions(self):
        """Handle viewing transaction history."""
        print("\n--- View Transaction History ---")
        account_number = self.get_input("Enter account number: ", str)
        
        account = self.bank.get_account(account_number)
        if not account:
            print(f"Error: Account {account_number} not found")
            return
        
        account.display_transactions()
    
    def view_customer_details(self):
        """Handle viewing customer details."""
        print("\n--- View Customer Details ---")
        customer_id = self.get_input("Enter customer ID: ", str)
        
        customer = self.bank.get_customer(customer_id)
        if not customer:
            print(f"Error: Customer {customer_id} not found")
            return
        
        customer.display_info()
    
    def update_customer_info(self):
        """Handle updating customer information."""
        print("\n--- Update Customer Information ---")
        customer_id = self.get_input("Enter customer ID: ", str)
        
        customer = self.bank.get_customer(customer_id)
        if not customer:
            print(f"Error: Customer {customer_id} not found")
            return
        
        print("\nWhat would you like to update?")
        print("1. Email")
        print("2. Phone")
        print("3. Address")
        choice = self.get_input("Enter choice: ", str)
        
        if choice == "1":
            new_email = self.get_input("Enter new email: ", str)
            customer.update_email(new_email)
        elif choice == "2":
            new_phone = self.get_input("Enter new phone: ", str)
            customer.update_phone(new_phone)
        elif choice == "3":
            new_address = self.get_input("Enter new address: ", str)
            customer.update_address(new_address)
        else:
            print("Invalid choice")
    
    def delete_account(self):
        """Handle account deletion."""
        print("\n--- Delete Account ---")
        account_number = self.get_input("Enter account number: ", str)
        
        account = self.bank.get_account(account_number)
        if not account:
            print(f"Error: Account {account_number} not found")
            return
        
        print(f"\nAccount: {account_number}")
        print(f"Customer: {account.customer_name}")
        print(f"Balance: ${account.balance:.2f}")
        
        confirm = self.get_input("\nAre you sure you want to delete this account? (yes/no): ", str)
        if confirm.lower() == "yes":
            self.bank.delete_account(account_number)
    
    def run(self):
        """Run the main application loop."""
        print("\nWelcome to Banking Management System!")
        
        while self.running:
            self.display_menu()
            choice = self.get_input("\nEnter your choice: ", str)
            
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.create_customer()
            elif choice == "3":
                self.deposit_money()
            elif choice == "4":
                self.withdraw_money()
            elif choice == "5":
                self.check_balance()
            elif choice == "6":
                self.view_account_details()
            elif choice == "7":
                self.view_transactions()
            elif choice == "8":
                self.view_customer_details()
            elif choice == "9":
                self.update_customer_info()
            elif choice == "10":
                self.bank.list_all_accounts()
            elif choice == "11":
                self.bank.list_all_customers()
            elif choice == "12":
                self.bank.display_bank_summary()
            elif choice == "13":
                self.delete_account()
            elif choice == "0":
                print("\nThank you for using Banking Management System!")
                print("Goodbye!")
                self.running = False
            else:
                print("\nInvalid choice. Please try again.")


def main():
    """Main entry point of the application."""
    app = BankingApp()
    app.run()


if __name__ == "__main__":
    main()
