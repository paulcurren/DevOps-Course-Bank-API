"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):

    response = client.post('/accounts/Name1')
    json = response.json

    assert response.status_code == 200
    assert json['name'] == 'Name1'

    response2 = client.get('/accounts/Name1')
    json2 = response2.json

    assert response2.status_code == 200
    assert json2['name'] == 'Name1'

def test_bank_report(client: FlaskClient):

    client.post('/accounts/Name1')
    client.post('/money', json = {'name': 'Name1', 'amount': 1})
    client.post('/money', json = {'name': 'Name1', 'amount': 2})

    response = client.get('/balance/Name1')
    json = response.json

    assert response.status_code == 200
    assert json == 3

