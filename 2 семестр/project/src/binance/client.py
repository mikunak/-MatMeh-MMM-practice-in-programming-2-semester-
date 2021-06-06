import requests
from datetime import datetime, timedelta


class Client:
    API_URL = 'https://api.binance.com/api/{v}/{path}'

    def __init__(self, api_key=None, secret_key=None):
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key

        self.session = self.init_session()

    def get_headers(self):
        """Получение нужных хедеров для работы с биржей"""
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36'
        }

        if self.API_KEY:
            headers['X-MBX-APIKEY'] = self.API_KEY
        return headers

    def init_session(self):
        """Инициализация сессии"""
        headers = self.get_headers()

        session = requests.session()
        session.headers.update(headers)
        return session

    def make_api_url(self, path):
        url = self.API_URL.format(
            v='v3',
            path=path
        )
        return url

    @staticmethod
    def handle_response(self, response: requests.Response):
        return response.json()

    def request(self, method, path, **kwargs):
        """Сделать запрос к бирже"""
        url = self.make_api_url(path)
        response = getattr(self.session, method)(url, **kwargs)
        return self.handle_response(self, response)

    def get(self, path, **kwargs):
        """Гет-запрос"""
        return self.request('get', path, **kwargs)

    def get_price(self, **params):
        """
        Получить текущую цену
        params = {
            'symbol': ...
        }

        https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker
        """

        path = f'ticker/price'
        js = self.get(path, params=params)
        return float(js['price'])

    def get_ticker_24hr(self, **params):
        """
        Получить изменение цены символа за последние 24 часа в процентом соотоношении
        params = {
            'symbol': ...
        }

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics
        """

        path = 'ticker/24hr'
        js = self.get(path, params=params)
        return js['priceChangePercent']

    def get_aggregate_trades(self, **params):
        """
        Получить список общий список трейдов
        params = {
            'symbol': ...,
            'fromId': ...,
            'startTime': ...,
            'endTime': ...,
            'limit': ...
        }

        https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list
        """

        path = 'aggTrades'
        js = self.get(path, params=params)
        return js

    def get_klines(self, **params):
        """
        Получить список klines/candlesticks для символа
        params = {
            'symbol': ...,
            'interval': ...,
            'startTime': ...,
            'endTime': ...,
            'limit': ...
        }

        https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data
        """

        path = 'klines'
        js = self.get(path, params=params)
        return js

    def get_ticker(self, data: datetime, **params):
        """
        Получить цену коина за определенную дату
        params = {
            'symbol' : ...,
        }
        """

        start_timestamp = int(data.timestamp() * 1000)
        end_timestamp = int((data + timedelta(minutes=10)).timestamp() * 1000)

        trades = self.get_aggregate_trades(
            symbol=params['symbol'],
            startTime=start_timestamp,
            endTime=end_timestamp
        )

        print(trades)

        if len(trades) == 0:
            # Вероятно, была введена слишком ранняя дата
            return 0
        return float(trades[0]['p'])

    def get_ticker_1hr(self, **params):
        """
        Получить изменение цены символа за последний час в процентом соотношении
        params = {
            'symbol': ...
        }
        """
        current_price = self.get_price(**params)

        hour_ago = datetime.now() - timedelta(hours=1)
        hour_ago_price = self.get_ticker(hour_ago, **params)

        return (current_price - hour_ago_price) * 100 / hour_ago_price

    def get_ticker_7days(self, **params):
        """
        Получить изменение цены символа за последние 7 дней в процентом соотношении
        params = {
            'symbol': ...
        }
        """

        current_price = self.get_price(**params)

        week_ago = datetime.now() - timedelta(days=7)
        week_ago_price = self.get_ticker(week_ago, **params)

        return (current_price - week_ago_price) * 100 / week_ago_price

