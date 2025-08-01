# import telebot
# from time import sleep

# TOKEN = '8360441269:AAHDqoZtE4n-hyeLG7Hsv8bQFz6jtN3zCYQ'  # Replace with your bot's token

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, " Привет я бот. Чем могу помочь?")
   

# @bot.message_handler(content_types=['text'])
# def text (message):
#         if message.text == "Привет" or message.text == "привет":
#             bot.send_message(message.from_user.id, "Привет как ты?")
#         elif message.text == "все хорошо":
#             sleep(2)
#             bot.send_message(message.from_user.id, "Пойдет сам как?")

#         elif message.text == "какие новости?":
#             sleep(2)
#             bot.send_message(message.from_user.id, "Пока нет ")

#         elif message.text == "Что делаешь?":
#             sleep(2)
#             bot.send_message(message.from_user.id, "Данный момент общаюсь с тобой")
#         else:
#           bot.send_message(message.from_user.id, "ошибка")

# bot.infinity_polling()


