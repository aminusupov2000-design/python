save =""
instructions ='Ты помощник по математике. Решай пошагово, пиши кратко и понятно. В конце дай ответ. '
import telebot
import logging
from google import genai #возможно ошибка здесь 

client = genai.Client(api_key="AIzaSyDnagkgb9BZu6CFMttjZAA06qOIleiZNj0")


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)





bot=telebot.TeleBot('8374810935:AAGduBipbU_PgHGT3SBVziICNO4_5kzaSAg')

@bot.message_handler(content_types=['text'])
def save_text(message):
    global save
    save = message.text
    print(save)
    bot.send_message(message.chat.id, f"Вы написали: {save}")


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