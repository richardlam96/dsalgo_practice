from datetime import datetime

from comparable import Comparable

class Transaction(Comparable):
    """
    Transaction class that inherits from Comparable to allow comparisons
    of different values including value, date, etc.
    """

    def __init__(self, name="", date="0001-01-1", amount=0):
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount
        self.default_cmp_key = "name"   # tmp fix for clients using default

    # overload functions to change default key
    def less_than(self, other, key="name"):
        return super().less_than(other, key)


    def equal_to(self, other, key="name"):
        return super().equal_to(other, key)


    def greater_than(self, other, key="name"):
        return super().greater_than(other, key)


    def print_info(self):
        print(
            self.name,
            self.date.year,
            self.date.month,
            self.date.day,
            self.amount
        )
