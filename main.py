import telebot
from telebot import types
import pytz
from datetime import datetime

bot = telebot.TeleBot('6800749212:AAHrF3XyF6JVxneFnJaXpYR16ssG0iMhHwc')

country_timezones = {
    'США/Нью-Йорк': 'America/New_York',
    'США/Лос-Анджелес': 'America/Los_Angeles',
    'США/Аляска': 'America/Anchorage',
    'Россия/Москва': 'Europe/Moscow',
    'Россия/Екатеринбург': 'Asia/Yekaterinburg',
    'Россия/Новосибирск': 'Asia/Novosibirsk',
    'Великобритания': 'Europe/London',
    'Франция': 'Europe/Paris',
    'Польша': 'Europe/Warsaw',
    'Китай': 'Asia/Shanghai',
    'Япония': 'Asia/Tokyo',
    'Корея': 'Asia/Seoul',
    'Индия': 'Asia/Kolkata',

}

def generate_countries_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [types.KeyboardButton(text) for text in country_timezones.keys()]
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Это бот для практики от Князькова Эльдара. Он показывает мировое время во всех регионах мира.\nИспользуйте команду /time для выбора страны.')

@bot.message_handler(commands=['time'])
def send_welcome(message):
    bot.reply_to(message, "Выберите страну для получения текущего времени:", reply_markup=generate_countries_keyboard())

@bot.message_handler(func=lambda message: message.text in country_timezones.keys())
def send_time(message):
    country = message.text
    timezone = pytz.timezone(country_timezones[country])
    current_time = datetime.now(timezone).strftime('%d.%m.%Y %H:%M:%S')
    bot.reply_to(message, f"Текущее время в {country}: {current_time}")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Пожалуйста, выберите страну из предложенных кнопок.")

bot.infinity_polling()