class Product:
    """Product class, requires paramenters (id,name,price,quantity) has methods get_total_price() and display()"""

    def __init__(self,id,name,price,quantity):
        """Initializes to the values that were passed"""
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        """Returns the price multiplied by the quantity"""
        return self.price * self.quantity

    def display(self):
        """Displays the products name, quantity, and total price"""
        total_price = self.get_total_price()
        print("{} ({}) - ${:.2f}".format(self.name,self.quantity,total_price))