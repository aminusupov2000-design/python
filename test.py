import telebot

bot=telebot.TeleBot('8374810935:AAGduBipbU_PgHGT3SBVziICNO4_5kzaSAg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'')


#наблюдай сохранить файл забыл

bot.polling(non_stop=True)