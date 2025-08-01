# Функции в Python помогают организовать и повторно использовать код. 
# Они позволяют разбить программу на логические блоки, 
# чтобы сделать ее более читаемой и удобной в поддержке.
# принимает аргумент и возращает значение то есть результат

# #практика функция 
# def my_func():
#     print("hello world")

# my_func() #вызов Функции

# #2 практика args kvargs 

# def perso(name,age,year,height):
#     return name ,age ,year ,height

# print(person("Naruto",19,2006,180))

# # #3 практика args kvargs 

# def person(name,age,year,height):
#     return name ,age ,year ,height

# print(person("Naruto",19,2006,180,22,1,2,2,2,2))

# def person(**kwargs):
#     return kwargs

# print(person(name = "Naruto",age = 19,year = 2006,height = 180))

# виды ошибки

# a = 1 / 0
# print(a) # zeroerror

# # a = "hello world"
# # print(str(a)) #ошибка значения 

# def say_hello(*args):
#     for name in args:
#         print(f"Привет, {name}!")

# say_hello("Шавуха", "You men", "Мелкий")


# #Функция сложения
# def сложить(a, b):
#     return a + b

# # Функция умножения
# def умножить(a, b):
#     return a * b

# # Примеры использования:
# print("Сложение 5 + 5 =", сложить(5, 5))
# print("Умножение 5 * 4 =", умножить(5, 4))

# def проверить_возраст(возраст):
#     if возраст >= 18:
#         return "Вход разрешен"
#     else:
#         return "Вход запрещен"


# print(проверить_возраст(20))  # Вход разрешен
# print(проверить_возраст(17))  # Вход запрещен

# def найти_четные(список):
#     четные = []
#     for число in список:
#         if число % 2 == 0:
#             четные.append(число)
#     return четные

# # Пример:
# ввод = [1, 2, 3, 4, 5, 6]
# print("Четные числа:", найти_четные(ввод))  # [2, 4, 6]




