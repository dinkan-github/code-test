import random


# TODO: create a bank class with create functionality

class AbstractAccount(object):
    def __init__(self, type: str, rate: int, account_number: int):
        self.type = type
        # self.amount = 0
        self.rate = rate
        self.account_number = account_number

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, val):
        assert val > 0
        self.amount += val

    def withdraw(self, amount) -> int:
        if amount < 1:
            raise ValueError("amount should be greater than 1")
        elif self.amount < amount:
            raise ValueError(f"amount should be not greater than {self.amount}")
        self.amount -= amount
        return amount



