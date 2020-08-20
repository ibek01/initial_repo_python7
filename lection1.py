# string = "hello world !!!"
# new_string = string.split(' ')
# print(new_string)
# person = "oJhn Snow"
# new_person = person.split('o')
# print(new_person)

# furious = "Toroto"
# furious.split('0')
# new_furious = furious.split('o')
# print(new_furious[0:len(new_furious)-1])
# print(dir(furious))


furious = "Toroto"
print(furious.split('o'))
print(furious)
int_ = 12
int_[1]

# name = "Peter"
# # name[-1] = 'a'
# # print(name.replace('r', 'a'))
# print(name + "hello")
# print(name)


# Method isdigit() -- True False 
# digit_string = input("Enter your string: ")
# print(digit_string.isdigit())

# phone_number = input("Enter your number: ")
# if phone_number.isdigit():
#     if phone_number.startswith('996'):
#         print("Your number is correct")
#     else:
#         print("Your number is invalid")
# else:
#     print("Your number is not digit")

#isalpha() method
# alpha_string = input("Enter some string: ")
# print(alpha_string.isalpha())
# isalnum method 
# string = input("enter some data: ")
# print(string.isalnum())

# method islower() - нижний регистр - маленькие буквы
# name = input("Введите имя: ")
# print(name.islower())

#isupper() - верхний регистр - большие буквы
# document = input("Example JOHN CONNOR: ")
# if document.isupper():
#     print("Your data is correct, we saved in our database")
# else:
#     raise Exception("Error 400")

# string = '\n\t '
# print(string.isspace())
# method istitle() and method title()
# names = ['John', 'Raychel', 'peter', 'Samanda', 'Eldiar']
# new_names = []

# for name in names:
#     if name.istitle():
#         new_names.append(name)
#         # print(new_names)
#     else:
#         new_names.append(name.title())
# print("Old names",names)
# # print("New names",new_names)
# sentence = "Hello world my name is John"
# new_sentence = sentence.title()
# print(new_sentence)
# print(new_sentence.istitle())

# # methods lower() and upper()
# caps_name = "john"
# # result --- JOHN
# print(caps_name.upper())
# lower_case_name = "JOHN"
# # result --- john
# print(lower_case_name.lower())
# method startswith() and endtswith()

# database = ['john', 'raychel']
# emails = ['johnsnow@gmail.com', 'raychel@gmail.com']
# username = input("Enter your username: ")
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# hash_password = []
# if email.endswith('@gmail.com'):
#     if username in database and email in emails:
#         print("Access!!!")
#         hash_password.append((hash(password)))
#     else:
#         print("User is not defined")
# else:
#     print("Ypur email is not correct")

# print(username,email, hash_password[0])

# lists_code = {"+996": "KG", "RU": "+7", "NA": "+31", "CH": "+8", "US": "+1"}

# number = input("Enter your number: ")
# for num in lists_code:
#     if number.startswith('+996'):
#         print(lists_code[num])
#     else:
#         continue

# dots = ','
# numbers = ['1', '2', '3']
# my_str = dots.join(numbers)
# print(my_str)
# method join()

# import os 
# print(os.path.dirname('lections'))
# slash = '/'
# lists_folder_name = ["my_project","templates", "products"]
# path = slash.join(lists_folder_name)
# print(path)
# absolute_path = os.path.abspath(path)
# print(absolute_path)


# print(ord('h'))
# print(chr(104))
# print(ord('d'))
# print(ord('D'))
# print(ord('A'))

# lists_alpha = ['a', "c", "d", "b"]
# new_lists_alpha = []
# for alpha in lists_alpha:
#     try:
#         if ord(alpha) < ord(lists_alpha[lists_alpha.index(alpha)+1]):
#             new_lists_alpha.append(alpha)
#         else:
#             continue
#     except IndexError:
#         print("Error")
# print(new_lists_alpha)

# lists_alpha = ['a', "c", "d", "b"] ---> ["a", "b", "c", "d"]
# hello = "hello"

# print("hello world".capitalize())

# print(ord('.'))


# string = "hellolo"
# print(string.count('lo', 4))

# string = "         Python                      is best language      "
# # print(string)
# # print(string.lstrip())
# # print(string.rstrip())
# # print(string.strip())
# print(string.replace(' ', ''))

# string = "hElLo"
# print(string.swapcase())

# print(dir("hello"))


# GET - "http://some.kg/?search_title=привет"
# GET - "http://some.kg/?search_title=%@a243"