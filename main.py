import os
import telebot


bot = telebot.TeleBot("1917134232:AAHqAiymbdZfOWTQgc4VLKv5qF4HYasKa9g")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm AK chat bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id)



bot.polling()
