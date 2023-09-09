# #Задача 1
# class DataBase:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")
#
#     def close(self):
#         print("закрытие соединения с БД")
#
#     def read(self):
#         return "данные из БД"
#
#     def write(self, data):
#         print(f"запись в БД {data}")
#
#
# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)
# print(db is db2)
# True


# #Задача 2
# class House():
#     def __init__(self, price):
#         self._price = price
#
#     @property
#     def price(self):
#         print(self._price)
#
#     @price.setter
#     def price(self, new_price):
#         if new_price > 0:
#             self._price = new_price
#         else:
#             print("Пожалуйста, введите корректное значение")
#
#     @price.deleter
#     def price(self):
#         delattr(self, '_price')
#
#
# house = House(50000.0)
# house.price  #50000.0
#
# house.price = 45000.0  # обновили значение
# house.price #45000.0
#
# house.price = -50 #Пожалуйста, введите корректное значение
#
# house.price #45000.0
#
# del house.price
# house.price #AttributeError: 'House' object has no attribute '_price'.


#Задача 3
from datetime import datetime
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_time_str):
        date_time_obj = datetime.strptime(date_time_str, '%d-%m-%Y')
        day = date_time_obj.day
        month = date_time_obj.month
        year = date_time_obj.year
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date_time_str):
        try:
            datetime.strptime(date_time_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False


date = Date.from_string('23-09-2022')
print(date.day)

print(Date.is_date_valid('23-15-2022'))