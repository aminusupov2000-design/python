import telebot
instructions ='Ты помощник по математике. Решай пошагово, пиши кратко и понятно. В конце дай ответ. '
bot=telebot.TeleBot('8374810935:AAGduBipbU_PgHGT3SBVziICNO4_5kzaSAg')

    

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id,'вы отправили фото')
@bot.message_handler(content_types=['text'])
def get_text(message):
    if len(message.text) > 3000:
        bot.send_message(message.chat.id, "Вы достигли лимита: максимум 3000 символов")
        return    
    bot.send_message (message.chat.id,'вы отправили текст')
        
    


bot.polling(non_stop=True)