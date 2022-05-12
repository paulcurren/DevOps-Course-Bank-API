from datetime import datetime
import pytest

from bank_api.bank import Account, Bank, Transaction
from bank_api.bank_report import BankReport


def test_report_no_transactions(monkeypatch):
    bank = Bank()
    bank_report = BankReport(bank)

    def mock_acc(name):
        return Account(name)
 
    monkeypatch.setattr(bank, 'get_account', mock_acc)

    balance = bank_report.get_balance('Name 1')

    assert balance == 0

def test_report_1_transactions(monkeypatch):
    bank = Bank()
    bank_report = BankReport(bank)

    def mock_acc(name):
        return Account(name)

    def mock_tx():
        transactions = []
        transactions.append(Transaction(Account('Name 1'), datetime.now(), 10))
        transactions.append(Transaction(Account('Name 1'), datetime.now(), 20))
        return transactions

    monkeypatch.setattr(bank, 'get_account', mock_acc)
    monkeypatch.setattr(bank, 'get_transactions', mock_tx)

    balance = bank_report.get_balance('Name 1')

    assert balance == 30

def test_report_2_transactions():
    bank = Bank()
    bank_report = BankReport(bank)

    bank.create_account('Name 1')
    bank.create_account('Name 2')
    bank.add_funds('Name 1', 1)
    bank.add_funds('Name 1', 2)
    bank.add_funds('Name 2', 2)

    balance = bank_report.get_balance('Name 1')

    assert balance == 3
