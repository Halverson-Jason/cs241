from product import Product

class Order:

    TAX = .065

    def __init__(self):
        """ Initializes to id="", and products to an empty list [] """
        self.id = ""
        self.products = []

    def get_subtotal(self):
        """ Sums the price of each product and returns it """
        total = 0.0
        for product in self.products:
            total = total + product.get_total_price()
        return total

    def get_tax(self):
        """ Returns 6.5% times the subtotal """
        return self.TAX * self.get_subtotal()

    def get_total(self):
        """Returns the subtotal plus the tax"""
        return self.get_subtotal() + self.get_tax()

    def add_product(self,product):
        """Adds the provided product to the list"""
        self.products.append(product)

    def display_receipt(self):
        """Displays a receipt"""

        print("Order: {}".format(self.id))

        for product in self.products:
            product.display()

        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))