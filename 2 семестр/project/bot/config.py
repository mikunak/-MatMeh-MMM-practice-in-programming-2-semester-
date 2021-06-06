"""
Конфигурационный файл бота
"""
from binance.currencies import MAINTAINED_COINS


# Токен телеграм-бота
BOT_TOKEN = '1758000737:AAFHgpyVMeYYub7qVB263GEl7i9an87RKfQ'

# Под какими ключами в словаре будут храниться веденные пользователем API и SECRET ключи
API_KEY_DICT_KEY = 'API_KEY'
SECRET_KEY_DICT_KEY = 'SECRET_KEY'

# Под какими ключами в словаре будут храниться веденная пользователем валюта и клиент биржи
USER_CURRENCY_KEY = 'currency'
BINANCE_CLIENT_KEY = 'binance'

# Под какими ключами в словаре буту храниться введенная пользователем желаемая валюта, её кол-во и дата для "мечтаний"
DREAMING_COIN = 'DREAMING_COIN'
DREAMING_VALUE = 'DREAMING_VALUE'
DREAMING_DATA = 'DREAMING_DATA'

# Формат ввода ключей в виде регулярного выражения
RE_KEYS_PATTERN = '^(.{64}):(.{64})$'


# Словарь для перевода наименований крипты в системе Binance в сообщения
FROM_SYMBOLS_TO_MESSAGE = {
    'BTC': 'Bitcoin',
    'LTC': 'Litecoin',
    'ETH': 'Ethereum',
    'BNB': 'Binance coin',
    'ADA': 'Cardano',
    'DOGE': 'Dogecoin',
    'XRP': 'Ripple',
    'LINK': 'Chainlink',
    'XLM': 'Stellar',
    'RUB': 'Rubles',
    'TUSD': 'Dollars',
    'EUR': 'Euros',
}
# Обратный
FROM_MESSAGES_TO_SYMBOLS = {
    v: k for k, v in FROM_SYMBOLS_TO_MESSAGE.items()
}

# Формат ввода коинов в виде регулярного выражения
RE_COINS_PATTERN = '^('
RE_COINS_PATTERN += '|'.join(FROM_MESSAGES_TO_SYMBOLS.keys())
RE_COINS_PATTERN += ')$'

# Формат ввода даты
DATA_FORMAT = 'YYYY-MM-DD'
DATETIME_FORMAT = '%Y-%m-%d'


class Messages:
    """Класс всех сообщений, которые может писать бот"""
    START = 'Привет! Я крипто бот!\nДля начала работы боту нужны ваши *API_KEY* и *SECRET_KEY* от площадки Binance'

    PROMPT_KEYS = 'Пожалуйста, введите ваш *API-* и *SECTER-*ключи в формате:\n`{API-KEY}:{SECRET-KEY}`'
    SHOW_KEYS = 'API Ключ: `{}`\nSecret Ключ: `{}`'
    BAD_KEYS_FORMAT = 'Неправильный формат ввода ключей! Попробуйте еще раз'
    ERROR_GETTING_KEYS = 'Произошла ошибка при получении ключей!'
    SAVED_KEYS = 'Ключи были успешно сохранены'

    CURRENT_CURRENCY = 'Текущая установленная валюта: {}'
    SAVED_CURRENCY = 'Валюта была успешно сохранена!'
    BAD_CURRENCY = 'Введена не поддерживаемая валюта!'

    COIN_PRICE = 'Цена {} на данный момент: {}'
    BAD_COIN = 'Введена не подерживаемая криптовалюта!'

    COIN_CHANGES = 'Изменение #{COIN_NAME}\nЗа последний час: {CHANGES_1HR}\nЗа 24 часа: {CHANGES_24H}\nЗа 7 дней: {CHANGES_7D}'
    """Площадка новая, api поддерживается только с этой даты"""
    DREAMING_DATE = 'Введите дату, когда Вы бы купили {DREAMING_COIN} в формате {DATA_FORMAT}\nВводите дату не раннее феврая 2020 года!'
    DREAMING_VALUE = 'Отлчино! Введите количество коинов, которое вы бы купили!'
    BAD_DATA_FORMAT = 'Неправильный формат даты!'
    DREAM = '#{COIN_NAME}\nТогда Вы бы потратили: {FORMER_WEALTH}\nА сегодня это стоит: {CURRENT_WEALTH}\nПроцентое соотношение: {RATIO}'
    DREAM_ERROR = 'Произошла ошибка! Вероятно, Вы ввели слишком раннюю дату!'


class ButtonTexts:
    """Класс всех текстов на кнопках меню"""
    ENTER_KEYS_TEXT = 'Ввести API- и SECRET-ключи для платформы Binance'
    SHOW_KEYS_TEXT = 'Посмотреть введенные API- и SECRET-ключи'

    SET_USER_VALUE_TEXT = 'Выбрать валюту, в которой показывать цены'

    SHOW_COINS_TEXT = 'Посмотреть текущие цены на криптовалюту'

    CHANGES_COINS_TEXT = 'Посмотреть изменения цен на криптовалюту'

    DREAMING_MSG = 'Мечтательная функция'

    BACK_TO_MAIN_MENU_TEXT = 'Назад'

