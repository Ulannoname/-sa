# Работа с файлами в Python

# Работа с файлами в Python включает открытие, чтение, запись и закрытие файлов.

# Основные режимы работы с файлами:

#   'r': Чтение файла (по умолчанию).
#   'w': Запись в файл (создаёт новый файл или очищает существующий).
#   'a': Добавление в файл.

# 1 практика запис в файл

with open("bootcamp 3.txt","w") as file:
    file.write("hello python") 

#     #практика чтения файла 

# with open("bootcamp - 3 txt","r") as files:
#     print("file.read"())

# # 3 практика добовления файла

# with open("bootcamp - 3.txt","a") as file:
#      file.write("index.html")

# # windows + r    cmd комаднный терминал


# name = input("Введите ваше имя: ")
# with open("users.txt", "a", encoding="utf-8") as file:
#     file.write(name + "\n")

# with open("users.txt", "r", encoding="utf-8") as file:
#     users = file.readlines()
#     for user in users:
#         print(user.strip())

 
# neee = input("Введите строку: ")

# if neee == "Python":
#     print("Верно")
# else:
#     print("Извините, но это неправильный ответ")

# name = input("Введите имя: ")
# surname = input("Введите фамилию: ")

# print(surname, name)

# colors = ["красный", "синий", "зеленый", "желтый", "фиолетовый"]

# print("Первый цвет:", colors[0])
# print("Последний цвет:", colors[-1])
