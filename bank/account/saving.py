from bank.account.base import AbstractAccount


class SavingAccount(AbstractAccount):
    def __init__(self, account_number):
        super().__init__('saving', 15, account_number)



