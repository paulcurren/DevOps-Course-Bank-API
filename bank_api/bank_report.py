
from bank_api.bank import Bank


class BankReport:
    bank: Bank

    def __init__(self, bank: str):
        self.bank = bank

    def get_balance(self, name: str) -> int:

        balance = 0
        transactions = list(filter(lambda transaction: transaction.account.name == name, self.bank.get_transactions()))

        for transaction in transactions:
            balance += transaction.amount

        return balance