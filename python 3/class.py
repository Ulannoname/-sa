# # Класс и обьект 

# # Класс — это шаблон (структура) для создания объектов.
# # Объекты — это конкретные экземпляры класса, которые имеют свойства (атрибуты) и действия (методы).


#   # 1.  Объединение данных и логики: Свойства и методы объединяются в одном блоке.
#   # 2.  Переиспользование кода: Можно создавать много объектов одного класса.
#   # 3.  Упрощение работы: Код становится структурированным и понятным.
#   # 4.  ООП: Классы — основа объектно-ориентированного программирования (ООП).




# class Car:
#     def __init__(self,name,model,year,price):
#         self.name = name
#         self.module = model
#         self.year = year
#         self.price = price
#     def info(self):
#         print(f"Название машины {self.name} Модель {self.module} год выпуска {self.year} Цена {self.price} ")

# object = Car("BMW","M5 E34 V12",2019,845000)
# object.info()











# class work 

# создать класс c названием Tank
# добавить 5 атрибутов
# добавить 1 метод
# вызваете класс и метод







# Создание класса Tank
# Класс Tank
class Tank:
    def __init__(self, name, model, armor, firepower, speed):
        self.name = name
        self.model = model
        self.armor = armor
        self.firepower = firepower
        self.speed = speed

    def info(self):
        print(f"Название танка - {self.name} Модель - {self.model} Броня - {self.armor} Огневая мощь - {self.firepower} Скорость - {self.speed} км/ч  ")
        


tank1 = Tank("T-90", "MS", 850, "100%", 65)
tank1.info()

