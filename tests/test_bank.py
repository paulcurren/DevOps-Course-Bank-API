"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

# TODO: Add unit tests for bank.add_funds()

def test_add_funds_no_account(bank: Bank):
    with pytest.raises(ValueError):
        bank.add_funds('no account', 1)

def test_add_funds_valid_account(bank: Bank):
    bank.create_account('Name 1')
    bank.create_account('Name 2')
    bank.add_funds('Name 1', 1)
    bank.add_funds('Name 2', 2)

    transactions = list(filter(lambda transaction: transaction.account.name == 'Name 1', bank.transactions))

    assert len(transactions) == 1
    assert transactions[0].amount == 1

def test_add_funds_valid_account_2_transactions(bank: Bank):
    bank.create_account('Name 1')
    bank.add_funds('Name 1', 1)
    bank.add_funds('Name 1', -2)

    transactions = list(filter(lambda transaction: transaction.account.name == 'Name 1', bank.transactions))

    assert len(transactions) == 2
    assert transactions[0].amount == 1
    assert transactions[1].amount == -2

