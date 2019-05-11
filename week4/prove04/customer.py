from order import Order

class Customer:

    def __init__(self):
        """Initializes to id="", name="", and orders to an empty list"""
        self.id = ""
        self.name = ""
        self.orders=[]

    def get_order_count(self):
        """Returns the number of orders"""
        return len(self.orders)

    def get_total(self):
        """Returns the total price of all orders combined"""

        total = 0

        for order in self.orders:
            total = total + order.get_total()
        return total

    def add_order(self,order):
        """Adds the provided order to the list of orders"""
        self.orders.append(order)

    def display_summary(self):
        """Displays a summary"""

        print("Summary for customer \'{}\':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))

    def display_receipts(self):
        """Displays all the orders' receipts"""

        print("Detailed receipts for customer \'{}\':".format(self.id))
        print("Name: {}".format(self.name))

        for order in self.orders:
            print()
            order.display_receipt()