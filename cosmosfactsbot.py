#загружаем библиотеки 
import telebot
from telebot import types
import random

 #добавляем токен
TOKEN = "8653523598:AAFunugzz0yG1NFjL-sjrvkUl4usx5I1Vzk"
bot = telebot.Telebot(TOKEN)

#пишем факты
facts = [
    "на луненет атмосферы"
    "в космосе нельзя услышать звук"
    "Несмотря на огромное расстояние в 150 миллионов километров, свет от Солнца достигает Земли всего за 8 минут и 20 секунд"
    "Температура на поверхности Венеры достигает 465°C, что горячее, чем на Меркурии, хотя Венера дальше от Солнца"
    "В условиях микрогравитации слезы не падают вниз, как на Земле, а остаются на глазах в виде маленьких капель"
    "Гора Олимп, находящаяся на Марсе, является самой высокой в Солнечной системе. Ее высота достигает 21 километра"
    "Венера вращается так медленно, что один полный оборот вокруг своей оси занимает больше времени, чем её оборот вокруг Солнца"
    "Юпитер делает один оборот вокруг своей оси всего за 10 часов. Из-за этого он слегка сплющен на полюсах"
]

#создаём для бота команду старт
@bot.message_handler(commands=['starts'])
def start(message):

    #создаём кнопку для получения факта
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("получить факт")
    keybord.add(btn)

    bot.send_message(message.chat.id,
                    "космические факты"
                    reply_markup=keybord)
@bot.message_handler(func=lambda message: True)
def fact(message):

    if message.text == "получить факт":
        bot.send_message(message.chat.id,
                        random.choise(fact))
        
bot.infinity_polling()
            
