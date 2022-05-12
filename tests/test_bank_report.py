import pytest

from bank_api.bank import Bank
from bank_api.bank_report import BankReport

@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_report_no_transactions(bank: Bank):

    bank_report = BankReport(bank)

    bank.create_account('Name 1')

    balance = bank_report.get_balance('Name 1')

    assert balance == 0

def test_report_1_transactions(bank: Bank):

    bank_report = BankReport(bank)

    bank.create_account('Name 1')
    bank.add_funds('Name 1', 1)

    balance = bank_report.get_balance('Name 1')

    assert balance == 1

def test_report_2_transactions(bank: Bank):

    bank_report = BankReport(bank)

    bank.create_account('Name 1')
    bank.create_account('Name 2')
    bank.add_funds('Name 1', 1)
    bank.add_funds('Name 1', 2)
    bank.add_funds('Name 2', 2)

    balance = bank_report.get_balance('Name 1')

    assert balance == 3
