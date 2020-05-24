# -*- coding: utf-8 -*-
import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь 🤔")

    markup.add(item1)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать юнным десигнерам.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def welcome_help(message):
    image = open('./screen_help.png', 'rb')
    bot.send_message(message.chat.id, "Как работать с ботом - <b>{1.first_name}</b>?\nОткройте в браузере изображения с сайта freepik.com, скопируйте цифры из URL и отправьте их боту".format(message.from_user, bot.get_me()),
        parse_mode='html')
    bot.send_photo(message.chat.id, image)

@bot.message_handler(content_types=['text'])
def send_document(message):
    if message.chat.type == 'private':
      if message.text == 'Помощь 🤔':
            bot.send_message(message.chat.id, '/help')
      else:
            bot.send_message(message.chat.id, 'Поиск')
            document = 'https://www.freepik.com/download-file/' + message.text
            bot.send_document(message.chat.id, document)

# Run
bot.polling(none_stop=True)
