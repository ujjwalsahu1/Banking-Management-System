"""Customer class for managing customer information in the banking system."""

class Customer:
    """Represents a bank customer with personal details."""
    
    def __init__(self, customer_id, name, email, phone, address):
        """
        Initialize a new customer.
        
        Args:
            customer_id (str): Unique identifier for the customer
            name (str): Customer's full name
            email (str): Customer's email address
            phone (str): Customer's phone number
            address (str): Customer's physical address
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    def update_details(self, name=None, email=None, phone=None, address=None):
        """
        Update customer details.
        
        Args:
            name (str, optional): New name
            email (str, optional): New email
            phone (str, optional): New phone
            address (str, optional): New address
        """
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
    
    def to_dict(self):
        """Convert customer to dictionary for storage."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create customer from dictionary."""
        return cls(
            data['customer_id'],
            data['name'],
            data['email'],
            data['phone'],
            data['address']
        )
    
    def __str__(self):
        """String representation of customer."""
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"
