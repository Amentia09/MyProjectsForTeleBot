
import telebot
from telebot import apihelper
from telebot import types


import config
bot = telebot.TeleBot(config.TOKEN)
apihelper.proxy = {'http':'http://anu-study.kz'}


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', '000')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Привет', '546', '000')

@bot.message_handler(commands=['start', 'help', 'web', 'ggwp', 'question'])
def send_welcome(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?", reply_markup=keyboard1)
	elif message.text == "/start":
		bot.send_message(message.from_user.id, "Есть некоторые команды: \n\n/start \n\n/web \n\n/ggwp \n\n/help \n\n/question", reply_markup=keyboard2)
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Есть некоторые команды: \n/start \n/web \n/ggwp \n/help \n\n/question")
	elif message.text == "/web":
		bot.send_message(message.from_user.id, "Поситите наш сайт по следующей ссылке: anu-study.kz", reply_markup=keyboard1)
	elif message.text == "/ggwp":
		bot.send_message(message.from_user.id, "Сорри фор бэд, диар исследователи)")
	elif message.text == "/question":
		keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
		key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
		keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
		key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
		keyboard.add(key_no);
		key_hz = types.InlineKeyboardButton(text='да хз', callback_data='hz')
		keyboard.add(key_hz)
		question = 'У тебя есть вопросы?';
		bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()
