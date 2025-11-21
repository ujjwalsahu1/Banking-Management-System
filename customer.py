"""Customer module for banking management system."""


class Customer:
    """Represents a bank customer with personal details."""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str, address: str = ""):
        """Initialize a new customer.
        
        Args:
            customer_id: Unique customer identifier
            name: Customer's full name
            email: Customer's email address
            phone: Customer's phone number
            address: Customer's address (optional)
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    def update_email(self, new_email: str):
        """Update customer email.
        
        Args:
            new_email: New email address
        """
        self.email = new_email
        print(f"Email updated to: {new_email}")
    
    def update_phone(self, new_phone: str):
        """Update customer phone number.
        
        Args:
            new_phone: New phone number
        """
        self.phone = new_phone
        print(f"Phone number updated to: {new_phone}")
    
    def update_address(self, new_address: str):
        """Update customer address.
        
        Args:
            new_address: New address
        """
        self.address = new_address
        print(f"Address updated to: {new_address}")
    
    def display_info(self):
        """Display customer information."""
        print("\n" + "="*50)
        print("CUSTOMER INFORMATION")
        print("="*50)
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address if self.address else 'Not provided'}")
        print("="*50)
    
    def __str__(self) -> str:
        """String representation of the customer."""
        return f"Customer({self.customer_id}, {self.name}, {self.email})"
    
    def __repr__(self) -> str:
        """Object representation of the customer."""
        return self.__str__()
