# name = "python programing"
# print(name)

# print (5 + 5)

# name = "said"
# print(name.upper()) #Вержний регистр
# print(name.lower()) #Нижний регистр
# print(name)

# # 1. Создайте данную строку
# text = "Сидел барсук в своей норе и ел картошечку пюре"

# # 2. Получите её длину
# length = len(text)
# print("Длина строки:", length)

# # 3. Проведите операцию сложения со строкой '.'
# new_text = text + '.'
# print("Строка после сложения с '.':", new_text)

# # 4. Проверьте, входит ли подстрока 'ре' в заданную строку
# contains_re = 'ре' in text
# print("Содержит 'ре'?", contains_re)

# # 5. Посчитайте количество вхождений подстроки 'ре'
# count_re = text.count('ре')
# print("Количество 'ре':", count_re)

# # 6. Получите первый символ строки
# first_char = text[0]
# print("Первый символ строки:", first_char)

# # 7. Получите все символы с нечётными индексами
# odd_index_chars = text[1::2]
# print("Символы с нечётными индексами:", odd_index_chars)

# # 8. Определите, сколько слов в строке
# word_count = len(text.split())
# print("Количество слов в строке:", word_count)

# # 9. Переверните строку
# reversed_text = text[::-1]
# print("Перевёрнутая строка:", reversed_text)

# # 10. Измените строку в нижнем регистре на верхний
# upper_text = text.upper()
# print("Строка в верхнем регистре:", upper_text)



# print("калькулятор на Python")
# print("Операции: +, -, *, /")


# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# op = input("Выберите операцию (+, -, *, /): ")

# #оператор
# if op == "+":
#     result = a + b
#     print("Результат:", result)
# elif op == "-":
#     result = a - b
#     print("Результат:", result)
# elif op == "*":
#     result = a * b
#     print("Результат:", result)
# elif op == "/":
#     if b != 0:
#         result = a / b
#         print("Результат:", result)
#     else:
#         print("Ошибка: деление на ноль!")
# else:
#     print("Ошибка: неизвестная операция")