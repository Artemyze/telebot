import telebot
from extensions import *
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Отправьте сообщение боту в виде <имя валюты, цену которой \n\
вы хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.\n\
Например: рубль доллар 20 \n\
Отправьте команду /values для ознакомления со списком поддерживаемых валют\n\
Отправьте команды /start /help для вывода справки(этого сообщения)')


@bot.message_handler(commands=['values'])
def echo_test(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys:
        text = '\n-- '.join((text, key))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def echo_test(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Введено не три параметра')
        qoute, base, amount = values
        total_price = Converter.get_price(qoute, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Не удалось обработать команду. {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду. {e}')
    else:
        bot.send_message(message.chat.id,\
                         f'Стоимость {float(amount):.2f} {qoute[:4]} в {base[:4]} равно {float(total_price):.2f}')


bot.polling()
