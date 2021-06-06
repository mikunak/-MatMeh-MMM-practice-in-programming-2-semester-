import pytest
from binance.client import Client


@pytest.fixture
def client():
    binance = Client()
    yield binance


def test_price(client: Client):
    """Проверка эндпоитна /ticker/price"""
    params = {
        'symbol': 'BTCTUSD'
    }
    price = client.get_price(**params)
    assert price > 0


def test_ticker_24hr(client: Client):
    """Проверка эндпоинта /ticker/24hr"""
    params = {
        'symbol': 'BTCTUSD',
    }
    price_change = client.get_ticker_24hr(**params)
    assert type(price_change) is float
