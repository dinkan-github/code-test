import random

from bank.account.current import CurrentAccount
from bank.account.saving import SavingAccount


class Bank(object):
    def __init__(self):
        self.account_number = 0
        self.type = None
        self.account = None
        self.name = None
        pass

    def create_account(self, name: str, type: str, initial_deposit: int, account_number: int):
        # TODO: validation be unique
        self.account_number = account_number
        self.name = name
        self.type = type

        if self.type == 'savings':
            self.account = SavingAccount(self.account_number)
            self.account.amount = initial_deposit
        elif self.type == 'current':
            self.account = CurrentAccount(self.account_number)
            self.account.amount = initial_deposit
        return self

    def get_accont(self, accont_number):
        # try the account
        self.account_number = accont_number

    def deposit(self, amount):
        # todo add validation
        self.account.amount += amount

    def withdraw(self, amount) -> int:
        self.account.amount -= amount
        return amount

    def account_info(self):
        # TODO: dataclass!
        return {
            'name': self.name,
            'type': self.type,
            'balance': self.account.amount or 0
        }
