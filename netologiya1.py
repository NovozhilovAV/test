# https://github.com/netology-code/guides/blob/master/repl/instruction.md

# Задание 1
# Напишите программу, которая последовательно запрашивает у пользователя
# Дату и Описание задачи, а затем выводит их через пробел..

# date1 = input("Введите дату: ")
# task1 = input("Ведите задачу: ")
# print(date1 + " " + task1)

# Задание 2
# Модифицируйте программу из задания 1 таким образом,
# чтобы запрос даты и задачи выполнялся трижды и после этого результаты
# выводились на экран построчно в формате:
# на одной строчке дата и задача через пробел..

# date1 = input("Введите дату: ")
# task1 = input("Ведите задачу: ")
# date2 = input("Введите дату: ")
# task2 = input("Ведите задачу: ")
# date3 = input("Введите дату: ")
# task3 = input("Ведите задачу: ")
# print(date1 + " " + task1)
# print(date2 + " " + task2)
# print(date3 + " " + task3)

# Задание 3
# Модифицируйте программу из задания 2 таким образом,
# чтобы данные не выводились на экран, а сохранялись в словарь.
# Ключами в этом словаре должны быть даты, а значениями - соответствующие им задачи..
# tasdate = {}
# date1 = input("Введите дату: ")
# task1 = input("Ведите задачу: ")
# tasdate[date1] = task1
# print(tasdate)
# date2 = input("Введите дату: ")
# task2 = input("Ведите задачу: ")
# tasdate[date2] = task2
# print(tasdate)
# date3 = input("Введите дату: ")
# task3 = input("Ведите задачу: ")
# tasdate[date3] = task3
# print(tasdate)

# name = input("Введите имя: ")
# login = "Dima"
# # name = "Yo"
# if name == login: # <- False
#   # Выражение True
#   print("Hello", name)
# elif len(name) < 3: # <- True
#   print("Такое имя недопустимо")
# elif name == "Yo": # <- True
#   print("Yo, bro")
# else:
#   # Выражение False
#   print("Hello, user!")
# print("The end")

# x = 1
# while x <= 10:
#   print(x)
#   x = x + 1
# print(x)

# Урок 2. Задание 1
# https://github.com/netology-code/pyfree-homeworks/blob/main/homeworks/2.md.
# Модифицируйте программу, написанную на занятии так,
# чтобы выход из нее осуществлялся не только при вводе неизвестной команды,
# но и при вводе специальной команды exit.
# Сделайте так, чтобы при вводе этой команды программа выводила на экран
# текст: "Спасибо за использование! До свидания!"

# Задание 2
# Давайте усложним нашу программу. Сделайте следующие изменения:
# Заведите 3 списка: today, tomorrow, other(можно назвать переменные по-другому).
# Измените блок кода, который выполняет команду add:
# Дополнительно запросите у пользователя дату выполнения задачи.
# В зависимости от введенной даты добавьте задачу в один из списков по следующим правилам:
# Если пользователь ввел "Сегодня", добавьте задачу в список today.
# Если пользователь ввел "Завтра", добавьте задачу в список tomorrow.
# Если пользователь ввел любое другое значение, добавьте задачу в список other.

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.
# random - добавить случайную задачу на сегодня
# """
# Random_task = 'Учиться програмированию'
# tasks = {}    # создаем словарь - задача/дата(ранее был список)
# today = []
# tomorrow = []
# other = []
# # создаем три списка - Сегодня-завтра -послезавтра
#
# while True:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#       dt = input("Введите дату для отображения задач : ")
#       if dt in tasks:
#           for task in tasks[dt]:
#               print(' - ', task)
#       else:
#           print('Такой даты нет! ')
#   elif command == "add":
#     task = input("Введите название задачи: ")
#     dt = input("Ведите дату выполнения задачи - сегодня/завтра/послезавтра : ")
#     if dt in tasks:
#         tasks[dt].append(task)   # если дата есть в словаре,добавляем задачу в список
#     else:
#         tasks[dt] = []
#         tasks[dt].append(task)    # даты в словаре неу,создаем запись с ключом даты
#     print(f'Задача ', task, ' на ', dt, ' добавлена!')
#   elif command == 'random':
#       if 'Сегодня' in tasks:
#           tasks['Сегодня'].append(Random_task)
#       else:
#           tasks['Сегодня'] = []
#           tasks['Сегодня'].append(Random_task)
#
#   elif command == "exit":
#       print("Спасибо за использование!")
#       break
#   else:
#     print("Неизвестная команда")
#     break
#
# print("До свидания!")

# решение от преподователя
# https://replit.com/@Netology/hw22#main.py
# today = list() # today = []
# tomorrow = list() # tomorrow = []
# other = list() # other = []

# HELP = '''
# Список доступных команд:
# * print  - напечать все задачи на заданную дату
# * todo - добавить задачу
# * help - Напечатать help
# '''

# while True:
#     command = input('Введите команду\n')
#     if command == 'help':
#         print(HELP)
#     elif command == 'todo':
#         date = input('Введите дату: ')
#         task = input('Введите задачу: ')
#         if date == 'Сегодня':
#           today.append(task)
#         elif date == 'Завтра':
#           tomorrow.append(task)
#         else:
#           other.append(task)
#         print(f'Задача {task} добавлена')
#     elif command == 'show':
#         print('Сегодня')
#         print(today)
#         print('Завтра')
#         print(tomorrow)
#         print('Другие')
#         print(other)
#     elif command == 'exit':
#         print('Спасибо за использование! До свидания!')
#         break
#     else:
#         print('Неизвестная команда!')
#         break.

# Урок №3 - используем функции
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавить случайную задачу на сегодня
"""
Random_task = 'Учиться програмированию'
tasks = {}    # создаем словарь - задача/дата(ранее был список)
today = []
tomorrow = []
other = []
# создаем три списка - Сегодня-завтра -послезавтра
# создадаим функцию и пропишем в ней
# повторяющийся участок кода для проверки словаря
# def add_todo(dt, task):
#     if dt in tasks:
#         tasks[dt].append(task)
#         # если дата есть в словаре,добавляем задачу в список
#     else:
#         tasks[dt] = []
#         tasks[dt].append(task)
#         # даты в словаре нету,создаем запись с ключом даты
#     print(f'Задача ', task, ' на ', dt, ' добавлена!')
#
#
# while True:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#       dt = input("Введите дату для отображения задач : ")
#       if dt in tasks:
#           for task in tasks[dt]:
#               print(' - ', task)
#       else:
#           print('Такой даты нет! ')
#
#   elif command == "add":
#     task = input("Введите название задачи: ")
#     add_todo(dt, tasks)
#
#   elif command == 'random':
#       add_todo('Сегодня', Random_task)
#
#   elif command == "exit":
#       print("Спасибо за использование!")
#       break
#   else:
#     print("Неизвестная команда")
#     break
#
# print("До свидания!")

# Домашнее задание к занятию 3. Функции. Разработка приложения
# https://github.com/netology-code/pyfree-homeworks/blob/main/homeworks/3.md
# Задание 1
# Реализуйте функцию count_letter, которая принимает список слов и некоторую букву
# и возвращает количество слов в списке, в которых эта буква встречается хотя бы один раз.
#
# Например, для списка ['python', 'c++', 'c', 'scala', 'java'] и буквы c ваша функция
# должна вернуть число 3.
# Подсказки
# Используйте конструкцию for word in ... для итерации по списку.
# Используйте переменную для хранения промежуточного результата подсчета.
# Используйте конструкцию letter in word для проверки наличия буквы в слове.

word = ['python', 'c++', 'c', 'scala', 'java']
wt = 'c'

def count_letter(word, wt):
    ct = 0
    for i in word:
        if wt in i:
            ct += 1

    return ct

a = count_letter(word, wt)
print(a)

# Решение от преподователя
# def count_letter(word_list, letter):
#   result = 0
#   for word in word_list:
#     if letter in word:
#       result += 1
#   return result
#
# print(count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c'))