from bot import updater
from bot.handlers import main_menu_handler

def main():
    # Добавить все хэндлеры
    updater.dispatcher.add_handler(main_menu_handler)

    # Начинает проверку на наличие новых сообщений от пользователей
    updater.start_polling()

    # Запуск до тех пор, пока не будет нажата комбинация клавиш CTRL+C
    updater.idle()


if __name__ == '__main__':
    main()
