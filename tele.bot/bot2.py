# # import telebot

# # TOKEN = '8380704178:AAFB77wwNAGOh4CHgRix_1Q8z1w72Tz2eWI'
# # bot = telebot.TeleBot(TOKEN)

# # # Создание клавиатуры
# # keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# # button1 = telebot.types.KeyboardButton('gucci')
# # button2 = telebot.types.KeyboardButton('perfume')
# # button3 = telebot.types.KeyboardButton('Video-Nike')
# # button4 = telebot.types.KeyboardButton('Help')
# # button5 = telebot.types.KeyboardButton('Audio')
# # keyboard.add(button1, button2, button3, button4, button5)

# # @bot.message_handler(commands=['start'])
# # def start(message):
# #     bot.send_message(message.chat.id, "Welcome to my shopping bot!", reply_markup=keyboard)

# # @bot.message_handler(func=lambda message: message.text == 'gucci')
# # def send_gucci(message):
# #     try:
# #         with open('photo_2025-07-31_17.jpg', 'rb') as img:
# #             bot.send_photo(message.chat.id, img, caption="This is the first shirt. Nice!")
# #     except FileNotFoundError:
# #         bot.send_message(message.chat.id, "Фото gucci не найдено!")

# # @bot.message_handler(func=lambda message: message.text == 'perfume')
# # def send_perfume(message):
# #     try:
# #         with open('photo_2025-07-31_17-52-52.jpg', 'rb') as img:
# #             bot.send_photo(message.chat.id, img, caption="бул жаны духи окшойт!")
# #     except FileNotFoundError:
# #         bot.send_message(message.chat.id, "Фото perfume не найдено!")

# # @bot.message_handler(func=lambda message: message.text == 'Video-Nike')
# # def send_video_nike(message):
# #     try:
# #         with open('АДЛИН - No Love.mp3', 'rb') as vid:
# #             bot.send_video(message.chat.id, vid, caption="Это видео.")
# #     except FileNotFoundError:
# #         bot.send_message(message.chat.id, "Видео не найдено!")

# # @bot.message_handler(func=lambda message: message.text == 'Help')
# # def send_help(message):
# #     bot.send_message(message.chat.id, "Нажми на кнопку чтобы посмотреть товары.")

# # @bot.message_handler(func=lambda message: message.text == 'Audio')
# # def save_audio(message):
# #     bot.send_message(message.chat.id, "Аудио сохранено.")

# # bot.infinity_polling()


# import random
# from telebot import Bot, Dispatcher, types, executor

# API_TOKEN = 'YOUR_TOKEN_HERE'

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# words = {
#     "apple": "яблоко",
#     "house": "дом",
#     "dog": "собака",
#     "sun": "солнце"
# }

# user_stats = {}

# @dp.message_handler(commands=['word'])
# async def send_word(message: types.Message):
#     word, translation = random.choice(list(words.items()))
#     await message.answer(f"{word} — {translation}")

# @dp.message_handler(commands=['quiz'])
# async def quiz(message: types.Message):
#     word, correct = random.choice(list(words.items()))
#     options = random.sample(list(words.values()), 3)
#     if correct not in options:
#         options[random.randint(0, 2)] = correct
#     user_stats[message.from_user.id] = {"word": word, "correct": correct}
#     await message.answer(f"Как переводится слово: *{word}*?\nВарианты:\n" + "\n".join(options))

# @dp.message_handler(commands=['answer'])
# async def check_answer(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_stats:
#         await message.answer("Сначала начните викторину с /quiz.")
#         return
#     user_answer = message.get_args().strip()
#     correct = user_stats[user_id]["correct"]
#     if user_answer.lower() == correct.lower():
#         await message.answer("✅ Правильно!")
#     else:
#         await message.answer(f"❌ Неверно. Правильный ответ: {correct}")
#     del user_stats[user_id]

# @dp.message_handler(commands=['stats'])
# async def stats(message: types.Message):
#     # Пример — можно хранить счет и показывать
#     await message.answer("Пока статистика не реализована 😅")

#     user_game_data = {}

# @dp.message_handler(commands=['startgame'])
# async def start_game(message: types.Message):
#     user_id = message.from_user.id
#     number = random.randint(1, 100)
#     user_game_data[user_id] = number
#     await message.answer("Я загадал число от 1 до 100. Попробуй угадать!")

# @dp.message_handler(commands=['guess'])
# async def guess(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_game_data:
#         await message.answer("Сначала начни игру с /startgame.")
#         return
#     try:
#         guess = int(message.get_args())
#     except ValueError:
#         await message.answer("Введите число после команды /guess.")
#         return

#     secret = user_game_data[user_id]
#     if guess < secret:
#         await message.answer("Моё число больше 📈")
#     elif guess > secret:
#         await message.answer("Моё число меньше 📉")
#     else:
#         await message.answer("🎉 Угадал! Можешь сыграть снова с /startgame.")
#         del user_game_data[user_id]

# @dp.message_handler(commands=['reset'])
# async def reset_game(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in user_game_data:
#         del user_game_data[user_id]
#     await message.answer("Игра сброшена. Введи /startgame чтобы начать заново.")

import os
import random
from telebot import TeleBot, types

API_TOKEN = '8394322334:AAE_9ssGuMblNBkgerLIvVZtrfSbjYQU0SM'

bot = TeleBot(API_TOKEN)

# --- Английский учитель ---
words = {
    "apple": "яблоко",
    "house": "дом",
    "dog": "собака",
    "sun": "солнце"
}

user_stats = {}
user_game_data = {}

@bot.message_handler(commands=['word'])
def send_word(message):
    word, translation = random.choice(list(words.items()))
    bot.send_message(message.chat.id, f"{word} — {translation}")

@bot.message_handler(commands=['quiz'])
def quiz(message):
    word, correct = random.choice(list(words.items()))
    options = random.sample(list(words.values()), 3)
    if correct not in options:
        options[random.randint(0, 2)] = correct
    user_stats[message.from_user.id] = {"word": word, "correct": correct}
    bot.send_message(
        message.chat.id,
        f"Как переводится слово: *{word}*?\nВарианты:\n" + "\n".join(options),
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['answer'])
def check_answer(message):
    user_id = message.from_user.id
    if user_id not in user_stats:
        bot.send_message(message.chat.id, "Сначала начните викторину с /quiz.")
        return
    user_answer = message.text.replace('/answer', '').strip()
    correct = user_stats[user_id]["correct"]
    if user_answer.lower() == correct.lower():
        bot.send_message(message.chat.id, " Правильно!")
    else:
        bot.send_message(message.chat.id, f" Неверно. Правильный ответ: {correct}")
    del user_stats[user_id]

@bot.message_handler(commands=['stats'])
def stats(message):
    # Пример — можно хранить счет и показывать
    bot.send_message(message.chat.id, "Пока статистика не реализована 😅")

# --- Игра "Угадай число" ---
@bot.message_handler(commands=['startgame'])
def start_game(message):
    user_id = message.from_user.id
    number = random.randint(1, 100)
    user_game_data[user_id] = number
    bot.send_message(message.chat.id, "Я загадал число от 1 до 100. Попробуй угадать!")

@bot.message_handler(commands=['guess'])
def guess(message):
    user_id = message.from_user.id
    if user_id not in user_game_data:
        bot.send_message(message.chat.id, "Сначала начни игру с /startgame.")
        return
    try:
        guess = int(message.text.replace('/guess', '').strip())
    except ValueError:
        bot.send_message(message.chat.id, "Введите число после команды /guess.")
        return

    secret = user_game_data[user_id]
    if guess < secret:
        bot.send_message(message.chat.id, "Моё число больше ")
    elif guess > secret:
        bot.send_message(message.chat.id, "Моё число меньше ")
    else:
        bot.send_message(message.chat.id, "🎉 Угадал! Можешь сыграть снова с /startgame.")
        del user_game_data[user_id]

@bot.message_handler(commands=['reset'])
def reset_game(message):
    user_id = message.from_user.id
    if user_id in user_game_data:
        del user_game_data[user_id]
    bot.send_message(message.chat.id, "Игра сброшена. Введи /startgame чтобы начать заново.")

# --- Загрузка файлов ---
UPLOADS_DIR = "uploads"
if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR)

@bot.message_handler(content_types=['photo', 'document'])
def handle_files(message):
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[-1].file_id)
        file_ext = '.jpg'
        file_name = f"photo_{message.from_user.id}_{message.message_id}{file_ext}"
    elif message.content_type == 'document':
        file_info = bot.get_file(message.document.file_id)
        file_name = message.document.file_name or f"document_{message.from_user.id}_{message.message_id}"
    else:
        return

    downloaded_file = bot.download_file(file_info.file_path)
    file_path = os.path.join(UPLOADS_DIR, file_name)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, "Файл сохранен!")

bot.polling(none_stop=True)
























