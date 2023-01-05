from bank.account.base import AbstractAccount


class CurrentAccount(AbstractAccount):
    def __init__(self, account_number):
        super().__init__('current', 10, account_number)



