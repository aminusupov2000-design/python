instructions ='Ты помощник по математике. Решай пошагово, пиши кратко и понятно. В конце дай ответ. '
import telebot
import logging
from datetime import datetime

import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)





bot=telebot.TeleBot('8374810935:AAGduBipbU_PgHGT3SBVziICNO4_5kzaSAg')



@bot.message_handler(commands=['start'])
def main(message):
    logging.info("Name: %s, нажал /start", message.from_user.first_name)
    bot.send_message(message.chat.id,f'привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    logging.info("Name: %s, нажал /help", message.from_user.first_name)
    bot.send_message(message.chat.id,'')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id,'вы отправили фото')
@bot.message_handler(content_types=['text'])
def get_text(message):
    if len(message.text) > 1000:
        bot.send_message(message.chat.id, "Вы достигли лимита: максимум 1000 символов")
        return    
    bot.send_message (message.chat.id,'вы отправили текст')
        
bot.polling(non_stop=True)