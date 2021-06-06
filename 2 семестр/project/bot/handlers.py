from telegram import (
    ReplyKeyboardMarkup,
    Update,
    ParseMode
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler
)
from bot.config import (
    Messages,
    ButtonTexts,
    API_KEY_DICT_KEY,
    SECRET_KEY_DICT_KEY,
    RE_KEYS_PATTERN,
    RE_COINS_PATTERN,
    FROM_SYMBOLS_TO_MESSAGE,
    FROM_MESSAGES_TO_SYMBOLS,
    USER_CURRENCY_KEY,
    BINANCE_CLIENT_KEY,
    DREAMING_COIN,
    DREAMING_VALUE,
    DREAMING_DATA,
    DATA_FORMAT,
    DATETIME_FORMAT
)
from binance.currencies import MAINTAINED_COINS
from binance.currencies import USER_CURRENCIES
from binance.client import Client
import re
import datetime


def get_username(update: Update):
    """Вспомогающая функция, которая возвращает имя пользователя"""
    return update.message.from_user.username


def get_symbol(message):
    """Функуция, возвращаюшая символ биржи по сообщению"""
    return FROM_MESSAGES_TO_SYMBOLS[message]


def get_message(symbol):
    """Функция, возврашающая сообщение по символу биржи """
    return FROM_SYMBOLS_TO_MESSAGE[symbol]


def decorator_callbacks_factory(state):
    """Декоратор для того, чтобы использовать уже написанные функции для вывода менюшек но с другим выводом"""

    def decorator_callback(func):
        def wrapper(update: Update, context: CallbackContext):
            result = func(update, context)
            return state

        return wrapper

    return decorator_callback


"""Часть кода, посвященная главному меню"""

# Состояния диалога с ботом
MAIN_CHOOSING, TYPING_KEYS = range(2)

# Нижнее главное меню у пользователя
main_reply_keyboard = [
    [ButtonTexts.ENTER_KEYS_TEXT, ButtonTexts.SHOW_KEYS_TEXT],
    [ButtonTexts.SET_USER_VALUE_TEXT],
    [ButtonTexts.SHOW_COINS_TEXT],
    [ButtonTexts.CHANGES_COINS_TEXT],
    [ButtonTexts.DREAMING_MSG]
]
main_markup = ReplyKeyboardMarkup(main_reply_keyboard)


def show_main_menu(update: Update, context: CallbackContext, text='Меню'):
    update.message.reply_text(
        text=text,
        reply_markup=main_markup,
        parse_mode=ParseMode.MARKDOWN
    )
    return MAIN_CHOOSING


def start(update: Update, context: CallbackContext):
    """Старт бота, показ главного меню"""
    # Установка валюты по умолчанию и создание клиента
    context.user_data.update({
        USER_CURRENCY_KEY: USER_CURRENCIES[0],
        BINANCE_CLIENT_KEY: Client()
    })
    return show_main_menu(update, context, Messages.START)


def show_keys(update: Update, context: CallbackContext):
    """Вывести веденные раннее API и SECRET ключи"""
    if context.user_data.get(API_KEY_DICT_KEY) and context.user_data.get(SECRET_KEY_DICT_KEY):
        update.message.reply_text(
            text=Messages.SHOW_KEYS.format(
                context.user_data[API_KEY_DICT_KEY],
                context.user_data[SECRET_KEY_DICT_KEY]
            ),
            reply_markup=main_markup,
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        update.message.reply_text(
            text=Messages.ERROR_GETTING_KEYS,
            reply_markup=main_markup,
            parse_mode=ParseMode.MARKDOWN
        )

    return MAIN_CHOOSING


def prompt_for_keys(update: Update, context: CallbackContext):
    """Запрашивание ввода ключей"""
    update.message.reply_text(
        text=Messages.PROMPT_KEYS,
        # reply_markup=main_markup,
        parse_mode=ParseMode.MARKDOWN
    )
    return TYPING_KEYS


def save_keys(update: Update, context: CallbackContext):
    """
    Сохраняем введенные пользователем ключи для платформы Binance
    Формат ввода данных: {API-KEY}:{SECRET-KEY}
    """
    if re.search(RE_KEYS_PATTERN, update.message.text):
        api_key, secret_key = update.message.text.split(':')

        client: Client = context.user_data[BINANCE_CLIENT_KEY]
        client.API_KEY = api_key
        client.SECRET_KEY = secret_key

        return_text = Messages.SAVED_KEYS
        state = MAIN_CHOOSING
    else:
        return_text = Messages.BAD_KEYS_FORMAT
        state = MAIN_CHOOSING

    update.message.reply_text(
        text=return_text,
        reply_markup=main_markup,
        parse_mode=ParseMode.MARKDOWN
    )
    return state


"""Часть кода, посвященная меню с монетами"""

# Состояния беседы после того, как нажата кнопка "Посмотреть цены на коины"
COINS_CHOOSING = 2


def build_coins_markup():
    """Создание меню с доступными коинами"""
    coins_reply_keyboard = []
    for coin in MAINTAINED_COINS:
        coins_reply_keyboard.append([FROM_SYMBOLS_TO_MESSAGE[coin]])
    coins_reply_keyboard.append([ButtonTexts.BACK_TO_MAIN_MENU_TEXT])
    return ReplyKeyboardMarkup(coins_reply_keyboard)


coins_markup = build_coins_markup()


def show_available_coins(update: Update, context: CallbackContext):
    """Вывод меню с доступными для просмотра коинами"""
    update.message.reply_text(
        text='Coins',
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=coins_markup
    )
    return COINS_CHOOSING


def show_coin_price(update: Update, context: CallbackContext):
    client: Client = context.user_data[BINANCE_CLIENT_KEY]

    symbol = get_symbol(update.message.text) + context.user_data[USER_CURRENCY_KEY]
    price = client.get_price(symbol=symbol)
    text = Messages.COIN_PRICE.format(update.message.text, price)
    update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=coins_markup
    )

    return COINS_CHOOSING


"""Часть кода, посвященная меню выбора валюты пользователя"""

# Состояния беседы после того, как нажата кнопка "Выбрать валюту"
TYPING_CURRENCIES = 3


def build_currencies_markup():
    value_reply_keyboard = []
    for value in USER_CURRENCIES:
        value_reply_keyboard.append([FROM_SYMBOLS_TO_MESSAGE[value]])
    value_reply_keyboard.append([ButtonTexts.BACK_TO_MAIN_MENU_TEXT])
    return ReplyKeyboardMarkup(value_reply_keyboard)


currencies_markup = build_currencies_markup()


def show_currencies(update: Update, context: CallbackContext):
    """Показать меню выбора валют"""
    update.message.reply_text(
        text=Messages.CURRENT_CURRENCY.format(
            FROM_SYMBOLS_TO_MESSAGE[context.user_data[USER_CURRENCY_KEY]]),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=currencies_markup
    )
    return TYPING_CURRENCIES


def save_currency(update: Update, context: CallbackContext):
    """Сохранить введеную пользователем валюту"""
    if FROM_MESSAGES_TO_SYMBOLS.get(update.message.text):
        currency = FROM_MESSAGES_TO_SYMBOLS[update.message.text]
        if currency in USER_CURRENCIES:
            context.user_data.update({
                USER_CURRENCY_KEY: currency
            })
            text = Messages.CURRENT_CURRENCY.format(update.message.text)
        else:
            text = Messages.BAD_CURRENCY
    else:
        text = Messages.BAD_CURRENCY

    update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=currencies_markup
    )
    return TYPING_CURRENCIES


"""Меню изменений криптовалюты"""
COINS_CHANGES_CHOOSING = 4

changes_coins_menu = decorator_callbacks_factory(COINS_CHANGES_CHOOSING)(show_available_coins)


def show_coins_changes(update: Update, context: CallbackContext):
    """Показать изменения валюты за 24 часа и за 7 дней"""

    client: Client = context.user_data[BINANCE_CLIENT_KEY]
    symbol = get_symbol(update.message.text) + context.user_data[USER_CURRENCY_KEY]

    changes_1hr = client.get_ticker_1hr(symbol=symbol)
    changes_24h = client.get_ticker_24hr(symbol=symbol)
    changes_7d = client.get_ticker_7days(symbol=symbol)

    text = Messages.COIN_CHANGES.format(
        COIN_NAME=update.message.text,
        CHANGES_1HR=changes_1hr,
        CHANGES_24H=changes_24h,
        CHANGES_7D=changes_7d,
    )

    update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=coins_markup
    )

    return COINS_CHANGES_CHOOSING


"""Меню мечтательной функции"""

"""Создание хэндлера целого меню"""
COINS_DREAMING_CHOOSING, DATE_TYPING, DREAMING_COINS_VALUE = 5, 6, 7

dreaming_coins_menu = decorator_callbacks_factory(COINS_DREAMING_CHOOSING)(show_available_coins)


def save_dreaming_coin(update: Update, context: CallbackContext):
    """Сохранение монеты для мечтаний и переход к вводу даты"""

    context.user_data[DREAMING_COIN] = get_symbol(update.message.text)

    update.message.reply_text(
        text=Messages.DREAMING_DATE.format(
            DREAMING_COIN=get_symbol(update.message.text),
            DATA_FORMAT=DATA_FORMAT
        ),
        parse_mode=ParseMode.MARKDOWN,
    )

    return DATE_TYPING


def save_dreaming_date(update: Update, context: CallbackContext):
    """Сохранение даты, когда пользователь бы купил коин и переход к вводу количесва коинов"""

    try:
        data = datetime.datetime.strptime(update.message.text, DATETIME_FORMAT)
        data += datetime.timedelta(hours=12)
        text = Messages.DREAMING_VALUE
        context.user_data[DREAMING_DATA] = data
    except ValueError:
        text = Messages.BAD_DATA_FORMAT

    update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN
    )

    return DREAMING_COINS_VALUE if text == Messages.DREAMING_VALUE else DATE_TYPING


def show_current_wealth(update: Update, context: CallbackContext):
    """Вывод текущего состояния"""

    client: Client = context.user_data[BINANCE_CLIENT_KEY]

    value = int(update.message.text)
    symbol = context.user_data[DREAMING_COIN] + context.user_data[USER_CURRENCY_KEY]
    current_price = client.get_price(symbol=symbol)
    former_price = client.get_ticker(
        data=context.user_data[DREAMING_DATA],
        symbol=symbol
    )
    if former_price == 0:
        text = Messages.DREAM_ERROR
    else:
        former_wealth = value * former_price
        current_wealth = value * current_price

        ratio = (current_wealth - former_wealth) / former_wealth * 100

        text = Messages.DREAM.format(
            COIN_NAME=context.user_data[DREAMING_COIN],
            FORMER_WEALTH=former_wealth,
            CURRENT_WEALTH=current_wealth,
            RATIO=ratio
        )

    update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=main_markup
    )

    return MAIN_CHOOSING


# TODO: Refactor
main_menu_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
    ],
    states={
        MAIN_CHOOSING: [
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.SHOW_KEYS_TEXT})$'), show_keys
            ),
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.ENTER_KEYS_TEXT})$'), prompt_for_keys
            ),
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.SHOW_COINS_TEXT})$'), show_available_coins
            ),
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.SET_USER_VALUE_TEXT})$'), show_currencies
            ),
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.CHANGES_COINS_TEXT})$'), changes_coins_menu
            ),
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.DREAMING_MSG})$'), dreaming_coins_menu
            )
        ],
        TYPING_CURRENCIES: [
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.BACK_TO_MAIN_MENU_TEXT})$'), show_main_menu
            ),
            MessageHandler(
                Filters.text, save_currency
            )
        ],
        TYPING_KEYS: [
            MessageHandler(
                Filters.text, save_keys,
            ),
        ],
        COINS_CHOOSING: [
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.BACK_TO_MAIN_MENU_TEXT})$'), show_main_menu
            ),
            MessageHandler(
                Filters.regex(RE_COINS_PATTERN), show_coin_price
            )
        ],
        COINS_CHANGES_CHOOSING: [
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.BACK_TO_MAIN_MENU_TEXT})$'), show_main_menu
            ),
            MessageHandler(
                Filters.regex(RE_COINS_PATTERN), show_coins_changes
            )
        ],
        COINS_DREAMING_CHOOSING: [
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.BACK_TO_MAIN_MENU_TEXT})$'), show_main_menu
            ),
            MessageHandler(
                Filters.regex(RE_COINS_PATTERN), save_dreaming_coin
            )
        ],
        DATE_TYPING: [
            MessageHandler(
                Filters.regex(f'^({ButtonTexts.BACK_TO_MAIN_MENU_TEXT})$'), show_main_menu
            ),
            MessageHandler(
                Filters.text, save_dreaming_date
            )
        ],
        DREAMING_COINS_VALUE: [
            MessageHandler(
                Filters.text, show_current_wealth
            )
        ]
    },
    fallbacks=[],
)
