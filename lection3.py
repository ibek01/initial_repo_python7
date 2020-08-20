## Dictionaries -- словарь

 # in other language Ассоциативные массивы
# Хэш таблицы

# data = {"key": "value"}
#Ключ только неизменяемые типы данных

# dict_ = {}
# print(type(dict_))
# dictionary_with_two_pairs = {
#     "key1": "hello", "key2": "world"
#     }
# print(type(dictionary_with_two_pairs))
# print(dictionary_with_two_pairs)
# dictionary_with_two_keyword_arguments = dict(
#     laptop = "Mac",
#     model = "Pro"
# )
# print(type(dictionary_with_two_keyword_arguments))
# print(dictionary_with_two_keyword_arguments)

# user_informations = {
#     "user1": {
#         "username": "John",
#         "age": 23,
#         "email": "john@bk.ru"
#     },
#     "user2": {
#         "username": "Raychel",
#         "age": 24,
#         "email": "raychel@bk.ru"
#     },
#     "user3": {
#         "username": "Peter",
#         "age": 25,
#         "email": "peter@bk.ru"
#     },

# }

# print(user_informations['user2']) #в запросе нужно указывать существующий ключ
# print(len(user_informations))

##Adding key with value 
# print("Before adding value", user_informations)
# user_informations['key4'] = 100 + 50
# print("After adding value", user_informations)

# user_informations['user1']['descriprion'] = 150 +50
# print(user_informations)


##Methods of Dictonary

# print(dir({}))


# code_country = {
#     "kg": "+996",
#     "kz": "+7",
#     "ru": "+8",
#     "us": "+1",
# }
# print(code_country['kg'])
# print(code_country.values())
# print(code_country.keys())

# info = {
#     "name": "John", "age": 25

# }
# info.fromkeys((
#     ("key1", "value1"),  "key2", "value2")
# print(info)

# x =('key1', 'key2', 'key3')
# y ="hello"

# thisdict = dict.fromkeys(x, y)

# print(thisdict)

# a_and_b_dictionary = dict.fromkeys(['a', 'b', ])
# print(a_and_b_dictionary)

# import random 
# lists_of_numbers = [x for x in range (1, 100)]
# random_data = dict.fromkeys(lists_of_numbers, random.choice
# (lists_of_numbers))
# print(random_data)

##Method get()
# cars = {
#     "car_name": "Honda",
#     "model": "Accord",
#     "year": "2008",
#     "odometr": 0
# }
# print(cars.get('car_name'))
# print(cars['car_name'])
# print(cars.get('key', "Error"))
# print(cars)

##Method items() возвращает и ключи и значения
# cars = {
#     "car_name": "Honda",
#     "model": "Accord",
#     "year": "2008",
#     "odometr": 0
# }
# for key, value in cars.items():
#     print(key, value)

##Method pop() удаляет о ключу и возвращает значение
# user_informations = {
#     "user1": {
#         "username": "John",
#         "age": 23,
#         "email": "john@bk.ru"
#     },
#     "user2": {
#         "username": "Raychel",
#         "age": 24,
#         "email": "raychel@bk.ru"
#     },
#     "user3": {
#         "username": "Peter",
#         "age": 25,
#         "email": "peter@bk.ru"
#     }
# }
# blocked_users = []
# user = user_informations.pop("user3")
# blocked_users.append(user)
# for x in blocked_users:
#     if x['username'] == "Peter":
#         user_informations["user4"] = x

# print(user_informations)
# print("All users in data base", user_informations)
# print("Blocked users in data base", blocked_users)


# fruits = {
#     'fruit1': "apple", "fruit2": "bananas"
# }
# fruits.pop()


##Method popitem() удаление из списка
# fruits = {
#     'fruit1': "apple", "fruit2": "bananas"
# }
# fruits.popitem()
# print(fruits)

##Method setdefault
# products = [ 
# { 
#     "title": "Macbook",
#     "category": "Computers",
#     "description": "Lorem ipsum",
#     "price": "1500$"
# },
# {
#    "title": "Acer",
#     "category": "Computers",
#     "description": "Lorem ipsum",
#     "price": "1000$" 
# },
# ]

# a = products[0].setdefault("hello", "world")
# print(a)
# print(products)

# tags = {
#     "tag1": "#hello"
# }
# tags.setdefault("tag0", "#world")
# print(tags)

##Method update()

# new_product = { 
#     "title": "Macbook",
#     "category": "Computers",
#     "description": "Lorem ipsum",
#     "price": "1500$"
# }

# old_product = {
#    "title": "Acer",
#     "category": "Computers",
#     "price": "1000$"
# }

# old_product.update(new_product)
# print(old_product)