import telebot
from telebot import types
from my_secrets import secrets


# передаём значение переменной с кодом экземпляру бота
token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

# глобальная переменная url
url = 'http://127.0.0.1:8000/'

# хендлер и функция для обработки команды /start
@bot.message_handler(commands = ['start'])
def start_message(message):
    # создаём кнопки бота
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    start_button = types.KeyboardButton("что я могу 😃 ")
    team_button = types.KeyboardButton("наша команда")
    new_button = types.KeyboardButton("посмотреть меню 📕")
    super_new_button = types.KeyboardButton("посмотреть акции 💃") 
    feedback_button = types.KeyboardButton("оставить отзыв") 
    special_offer_button = types.KeyboardButton("специальное предложение")
    
    markup.add(start_button, team_button, new_button, super_new_button, feedback_button, special_offer_button )
    # приветсвенное сообщение для команды /start
    bot.send_message(message.chat.id, text="Привет, {0.first_name} 👋\nВоспользуйся кнопками".format(message.from_user), reply_markup=markup)

# хендлер для обработки нажатий кнопок
@bot.message_handler(content_types = ['text'])
def buttons(message):
    if message.text == "что я могу 😃":
        bot.send_message(message.chat.id, text = "Я могу помочь заказать тебе пиццу, напитки и другие снэки!\nДля этого нажми на кнопку посмотреть меню")
    elif message.text == "наша команда":
        bot.send_message(message.chat.id, text = "@ddzyuba_m\n@karkusha05\n@Stilist_0\n@Paccifficul\n@z_masha_z\n")
    elif message.text == "посмотреть меню 📕":
        bot.send_message(message.chat.id, text = "посмотрим меню:", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("посмотрим", url = url + "products/")))
    elif message.text == "посмотреть акции 💃":
        bot.send_message(message.chat.id, text = "узнаем какие акции:", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("узнаем", url = url + "sales/")))
    elif message.text == "оставить отзыв": 
        bot.send_message(message.chat.id, text = "Напишите ваш отзыв:")
        bot.register_next_step_handler(message, process_feedback)
    elif message.text == "специальное предложение":  # обработка нажатия на кнопку "специальное предложение"
        with open('/opt/bot/photo.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, text = "Извини, я могу отвечать только на нажатие кнопок")

def process_feedback(message):
    # здесь происходит отправка отзыва администратору
    feedback_text = message.text
    bot.send_message(message.chat.id, text = "Спасибо за ваш отзыв!")
    
    # Отправка отзыва администратору
    admin_chat_id = '268074514'  # идентификатор чата администратора
    bot.send_message(admin_chat_id, text = f"Новый отзыв от {message.from_user.first_name} {message.from_user.last_name} (@{message.from_user.username}):\n{feedback_text}")




# бесконечное выполнение кода
bot.polling(none_stop = True, interval = 0)