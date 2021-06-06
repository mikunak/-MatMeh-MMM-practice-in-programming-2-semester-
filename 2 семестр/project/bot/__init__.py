from telegram.ext import Updater
from bot.config import BOT_TOKEN


updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
