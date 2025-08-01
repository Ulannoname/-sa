#список list изменянные данные
#[]

# Список методы

# list = ["alibek","ulan","umut"]
# list.append("Erbol") #Добавить
# list.remove("ulam") #Удалить
# list.insert(0,"Elnur") #посл место
# list.pop()
# #list.clear{}
# list.sort()
# print(list)
# 1
# list = [12, 34, 56, 78, 90]
# print(max(list))

# # 2
# list = [12, 34, 56, 78, 90]
# print(min(list))

# # 3
# list = [7, 6, 5, 4, 3, 2, 1, 0]
# print(sorted(list))

# # 4
# list = ['python', 'php', 'java', 'goolang']
# print(len(list))

# # 5
# list = ['python', 'php', 'java', 'goolang']
# list.append('html')
# print(list)
# Исходный список
# list = [1, 2, 3, 4, 5, 6, 7]


# list.append(8)
# print("После append:", list)


# list.pop(4)
# print("После pop:", list)


# list.insert(2, 3)
# print("После insert:", list)

# length = len(list)
# print("Длина списка:", length)


# list.clear()
# print("После clear:", lis


# import random 
# import time

# number = random.randint(1, 20)
# go = time.time()
# ptu = 0

# while True:
#      al = int(input("Угадай число 1,20: "))
#      ptu += 1
#      if al < number:
#          print("Больше")
#      elif al > number:
#        print("Меньше")
# else:
#     print(f"Угадал за {0} попыток!")
# print(f"Время: {round(time.time() - go, 2)} сек.")


# import random
# import time

# print("Добро пожаловать в игру 'Угадай число'!")
# print("Я загадал число от 1 до 20. Попробуй угадать его.")


# secret_number = random.randint(1, 20)


# start_time = time.time()


# attempts = 0

# while True:
#     try:
#         guess = int(input("Введите ваше предположение: "))
#         attempts += 1

#         if guess < secret_number:
#             print("Моё число больше.")
#         elif guess > secret_number:
#             print("Моё число меньше.")
#         else:
#             end_time = time.time()
#             elapsed_time = round(end_time - start_time, 2)
#             print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
#             print(f"Время, затраченное на игру: {elapsed_time} секунд.")
#             break
#     except ValueError:
#         print("Пожалуйста, введите целое число.")


# import pyfiglet
# name = input("Как тебя зовут? ")
# print(f"меня зовут,{name}")
# print(pyfiglet.figlet_format(font="slant",text=name))

# import pyfiglet
# import random
# name = input("Как тебя зовут? ")
# print(pyfiglet.figlet_format(name))
# print(name)
# compliment = ["Ты крут"]
# print(random.choice(compliment))
