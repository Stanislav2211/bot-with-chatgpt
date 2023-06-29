import telebot
import openai
gpt_key='*******************************************'
telegram_key='******************************************'

bot=telebot.TeleBot(telegram_key)
openai.api_key=gpt_key
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,f'Привіт,{message.from_user.username}. Бот запущено!')


@bot.message_handler(content_types=['text'])
def main(message):
    reply=''
    response=openai.Completion.create(
        engine='text-davinci-003',
        prompt=message.text,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    if response and response.choices:
        reply=response.choices[0].text.strip()
    else:
        reply='Something went wrong🥲🥲🥲'
    bot.send_message(message.chat.id,reply)

bot.polling(none_stop=True)
