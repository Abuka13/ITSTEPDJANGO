import telebot
from telebot import types
import json
import datetime
bot = telebot.TeleBot('6111880037:AAFr90nbxiE0VOIPPVoLeWviFanWggyM-AA')

ERROR_TEXT = "Произошла ошибка, попробуйте ещё раз или обратитесь к администратору"
DEBUG = False  # TODO debug == true - идёт разработка


def decorator_exception_1(func):
    def wrapper(*args, **kwargs):
        message: telebot.types.Message = args[0]
        try:
            func(*args, **kwargs)
        except Exception as error:
            _error = f"error: {error}"
            print(_error)
            with open("logs/errors.txt", mode="a", encoding="utf-8") as file:
                file.write(f"[{datetime.datetime.now()}] {error}\n")
            if DEBUG:
                bot.send_message(message.chat.id, _error, parse_mode='html')
            else:
                bot.send_message(message.chat.id, ERROR_TEXT, parse_mode='html')

    return wrapper


@decorator_exception_1
@bot.message_handler(commands=['start'])
def b_start(message):
    commands = """
    <strong>Привет! Я бот специализуюванный на публикации книг</strong>

    <b>Ниже список команд с описанием:</b>

    <i>Базовые</i>
    /start - начальное меню

    <i>Публикация книг</i>
    /publish - Публикация твоей новой книги
    """
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, commands, parse_mode='html', reply_markup=markup)


@decorator_exception_1
@bot.message_handler(commands=['publish'])
def b_publish(message):
    bot.send_message(message.chat.id,
                     """<b>Введите через запятую название книги,жанр книги,цена книги и имя автора: """)
    bot.register_next_step_handler(message, b_book)


def b_book(message: telebot.types.Message):
    data = message.text.split(",")

    title: str = data[0].strip().capitalize()
    genre: str = data[1].strip()
    price: float = float(data[2].strip())
    name: str = data[3].strip().capitalize()
    # print(title, count, price)

    with open("data/book.json", mode="r", encoding="utf-8") as file:
        books: list[dict] = json.load(file)
        books.append({"id": int(books[-1]["id"]) + 1, "title": title, "count": genre, "price": price, "name": name})

    with open("data/book.json", mode="w", encoding="utf-8") as file:
        json.dump(books, file)








if __name__ == "__main__":
    print("bot started...")
    try:
        bot.infinity_polling()
    except Exception as error:
        print("error: ", error)
    print("bot stopped...")