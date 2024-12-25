

###################  SET ######################

"""
set бир учурда оз ичине уникалдуу элементтерди сактай алат

"""

# myset = {1,1,1,2,3,7,4,5,5,5,9,9}
# myset.add(110)
# print(myset.clear())
#

#############################        DICTIONARY      ###########################

# my_dic = {'name': 'Uson', 'lastname':'Azizov'}
# mydic2 = {1:4, 2:6, 3:9}
# print(mydic2[1])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict['model'])
# print(thisdict['brand'])
# print(thisdict['year'])


########################### pop ###################

# """
#     pop создукту удалить кылуу
#
# """
# thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
# }
# thisdict.pop('model')
# print(thisdict)

###########################   Keys #########################

"""
ключ ачкычы создуктун 
 print(thisdict.keys()) только ачкычтарды алып берет 
"""

# thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
# }
# print(thisdict.keys())

######################### value ##################
"""
    value значениесы создуктун   мааниси
print(thisdict.values())  только маанилерин алып берет 

"""
# thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
# }
# print(thisdict.values())

"""

тапшырма     бир создук жаратып аты mydic болот ичине 1 ден баштап 100 чейин толтургула 
ачкычы мааниси деле ошол болот 

пример 

{1:1, 2:2, 3:3, ............99:99}

"""


#
# mydic = {}
#
# i = 2
# while i <= 100:
#     mydic[i] = i + 1
#     i += 2
# print(mydic)


# mydic = {}
# for i in range(2, 101, 2):
#     mydic[i] = i +1
# print(mydic)


# mydic = {
#     'apple': 'яблоко',
#     'banana': 'банан',
#     'cherry': 'вишня',
#     'kivi': 'киви'
# }
# word = input("Ведите слово на английском")
# translation = mydic.get(word, "слово не найдено")
# print(translation)
#

# Пример решения

#
# people = [
#     {"name":"Tom", "age":39, "company":"Supercorp", "languages": ["Python", "javaScropt"]},
#     {"name":"Bob", "age":43, "company":"BigCorp", "languages": ["Python", "c++","c#"]},
#     {"name":"Sam", "age":28, "company":"LittleCorp", "languages": ["Python", "java"]}
# ]
# search_name = input("Введите имя человека").strip()
# person_data = next((person for person in people if person['name'].lower() == search_name.lower()), None)
#
# if person_data :
#     print(f"Данные о {search_name}"
#           f"{person_data}")

#
# a = {"name":"Anna", "age": 25, "country":"russia"}
# b = input("Введите ключ для проверки")
# if b in a:
#     print(f"значение этого ключа :{a[b]}")
# else:
#     print("error")
#
# weekdays = {
#
#     "понедельник": 1,
#     "вторник": 2,
#     "среда": 3,
#     "четверг":4,
#     "пятница":5,
#     "суббота":6,
#     "воскресенье":7
#
# }
# print(weekdays)

"""

задание 1   
бир словарь тузгуло аны кайра очистить кылгыла тазалап салгыла

пример 
a = {1:2, 3:4, 5:6}
{}

задание 2 бир словарь жаратып  только значение чыгаргыла
пример 

a = {1:2, 3:4, 5:6}
{2,4,6}


задание 3

создать словарь  ключ name значение возрост этого человека и надо сделать так чтоб логика 
каждому возросту человека дабавилось по 5 лет 

пример 

a = {"Dima":40, "Uson": 15, "Esentur":17}

{"Dima":45, "Uson": 20, "Esentur":22}

"""









