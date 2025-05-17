from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    def __init__(self):
        self.items = []  # list of tuples (Item, quantity)
        self.datetime = None

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def finalize(self):
        self.datetime = datetime.now()

    @property
    def total_number(self):
        return sum(qty for _, qty in self.items)

    @property
    @abstractmethod
    def total_cost(self):
        pass

    @property
    def transaction_type(self):
        return self.__class__.__name__

class PurchaseOrder(Transaction):
    @property
    def total_cost(self):
        return sum(item.wholesale_price * qty for item, qty in self.items)

class CustomerSale(Transaction):
    @property
    def total_cost(self):
        return sum(item.retail_price * qty for item, qty in self.items)
