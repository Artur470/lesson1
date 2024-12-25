"""

"w": write    жазуу
"a": append   кошуу
"r": read     окуу

"""
from moduls import models
import os

# def save_data(file_name, data):
#     with open(file_name, "w")as file:
#         file.write(data)
#
# def append_data(file_name, data):
#     with open(file_name, "a")as file:
#         file.write(data)
#
# def read_data(file_name):
#     with open (file_name, "r")as file:
#         result = file.read()
#         return result
#
# def remove_file(file_name):
#     try:
#         os.remove(file_name)
#         return ('успешно удалено')
#     except:
#         return ('Ошибка')
#
def sum(a,b):
    result = a+b
    return result

