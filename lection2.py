# imutable - неизменяемые
# mutable -изменяемые 


# imutable
# numbers (int, long, float, complex)
# str, bool, frozenset, tuple

# mutable
# list, dictionary, set

# num = 5
# print(num) ---> 5
# num = "example"
# print(num) --> example

#List  and List Methods

# example_list = []
# example_list = [1, 2, 3, 4, 5]
# example_list = list()
# example_list = range() #start end step

# names = []
# print(type(names))


# numbers = list(range(1, 100, 2))
# print(numbers)

# a_list = ['a', 'b', [12, 11, 10], 'c', (1, 2)]
# print(a_list[2])
# print(len(a_list))

# print(dir([])) #вызов методов 

# method append () - добавляет элемент в конец списка

# carts = []
# list_of_goods = ['TV', 'smartphones', 'apple watch', 'laptop']
# add_to_cart = input(f'{list_of_goods}: ')
# add_to_cart = input(f'Choose goods {list_of_goods}: ')
# if add_to_cart:
#     carts.append(
#         list_of_goods.pop(
#             int(add_to_cart)
#         )
#         )
# print(f"There are {len(carts)} goods, name {carts}", )

#Method pop()
# laptops = ['Acer', 'Lenovo', 'Macbook', 'Del', 'HP', 'Asus']
# print("Before", laptops)
# laptops.pop(2)
# print("After", laptops)


# string vs list
# var = "hello world"
# print("Before", var)
# var + "My name is John"
# print("After", var)


# contacts = ['John', 'Peter', 'Raychel', 'Sandy']
# print("Before ", contacts)
# ignors_user = []
# user = contacts.pop(1)
# user2 = contacts.pop(2)
# ignors_user.append(user)
# ignors_user.append(user2)
# print("After", contacts)
# print("List of ignors", ignors_user)

##применение метода pop() при авторизации пользователя логин и пароль
# password = 123
# password_confirmation = 123
# some_json = ['username', '123', '123']
# password1 = some_json[1]
# password2 = some_json.pop(2)
# if password1 != password2:
#     raise Exception("Password not match")
# else:
#     print("Success")
#lifo fifo 
# numbers = [1, 2, 3, 4, 5]
# numbers.pop()
# print(numbers)

#Method extend()
# some_lists = ['Orange', 'Strawberry', ]
# lists = ['Bananas', 'Apples', 'Pineaples', ]
# lists.extend(some_lists)
# print(some_lists)
# print(lists)

##также extend() можно заменть на "+="
# some_lists = ['Orange', 'Strawberry', ]
# lists = ['Bananas', 'Apples', 'Pineaples', ]
# print(id(lists))
# # lists = lists + some_lists
# lists += some_lists
# print(id(lists))
# # print(some_lists)
# # print(lists)

##Method remove() удаление по элементу
# cars =['BMW', 'Mercedes', 'Audi', 'Honda']
# print(cars)
# cars.remove('BMW')
# print(cars)

##Method insert() 
# cars = ['BMW', 'Mercedes', 'Audi', 'Honda']
# print(cars)
# cars.insert(-10, 'Toyota')
# print(cars)


# list_of_phone_numbers = [
#     777, 777, 999, 999, 333, 444, 100
#     ]
# new_list_of_numbers = []

# for phone_number in list_of_phone_numbers:
#     if phone_number not in new_list_of_numbers:
#         new_list_of_numbers.append(phone_number)
#     else:
#         continue

# print(list_of_phone_numbers)
# print(new_list_of_numbers)

# list_of_phone_numbers = [
#     777, 777, 999, 999, 333, 444, 100
#     ]
# new_list_of_numbers = []

# for index, item in enumerate(list_of_phone_numbers):
#     # print(list_of_phone_numbers.index(x))
#     # x[0] == x[0+1]
#     if list_of_phone_numbers[index] == list_of_phone_numbers[index +
#     1]:
#         list_of_phone_numbers.pop(index)
#     else:
#         continue
# print(list_of_phone_numbers)

##Method count() считает количество повторений 
# cars =['BMW', 'Mercedes', 'Audi', 'Honda', 'Audi']
# print(cars.count('Audi'))


## Method reverse изменяет отображение списка задом наперед
# cars =['BMW', 'Mercedes', 'Audi', 'Honda']
# print(cars)
# cars.reverse()
# print(cars)

##Method clear() очистка списка
# cars =['BMW', 'Mercedes', 'Audi', 'Honda']
# cars.clear()
# print(cars)

##Method sort() сортирует список по алфавиту
# cars =['BMW', 'Mercedes', 'Audi', 'Honda']
# cars.sort()
# print(cars)

# def customFunc(x): #создание кастомной функции которая сортирует список по длине букв айтемов в списке
#     return len(x)
# cars =['BMW', 'Mercedes', 'Audi', 'Honda']
# cars.sort(key=customFunc)
# print(cars)


# list_of_phone_numbers = [
#      777, 777, 999, 999, 333, 444, 100
#      ]
# print(sorted(list_of_phone_numbers))
# print(list_of_phone_numbers)

# ls = [[1, 2, 3, [1, 2, 3]], [4, 5, 6], [7, 8, 9]]
# print(ls[0][3][1])

# ls =["hello", "word"]
# print(ls)
# ls[1] = "world"
# print(ls)

## Tuple --- Кортеж --- Неизменяемый тип данных -- ()
# shoplist = ('apple', 'mango', 'carrot', 'banana')
# print(type(shoplist))
# print(shoplist.index('apple'))
# print(shoplist.count('apple'))
# print(dir(shoplist))

# shoplist[0] = 'hello'

# tuples = (1, 2, 3, [1,2,3], 1.5, "hello")
# print(type(tuples))
# tuples[3][0] = "hello"
# print(tuples)

# ls = (1, ) #если есть запятая после айтема то тип данных -кортеж
# print(type(ls))

# ls = 1 #если нет заяптой после айтема, то тип - число
# print(type(ls))