import telebot
import json
bot = telebot.TeleBot('5841378271:AAGVPwqA0mknVI7vG1zXhPh94ldZvImhQtU')

from telebot import types
     
def _command_(message):
     bot.send_message(message.chat.id, "Введите имя: ")
     bot.register_next_step_handler(message, add_user)
def add_user(message):
     data = message.text
     bot.send_message(message.chat.id,data[::-1])
bot.infinity_polling()
