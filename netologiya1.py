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
#
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

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""
tasks = []
# создаем три списка
today = []
tomorrow = []
other = []

run = True
while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")

    dt = input("Ведите дату выполнения задачи - сегодня/завтра/после: ")
    if dt == "Сегодня":
        today.append(dt)
        print(f'Задача ' + task + ' на ' + dt + ' добавлена!')
    if dt == "Завтра":
        tomorrow.append(dt)
        print(f'Задача ' + task + ' на ' + dt + ' добавлена!')
    if dt == "После":
        other.append(dt)
        print(f'Задача ' + task + ' на ' + dt + ' добавлена!')

  elif command == "exit":
      print("Спасибо за использование!")
      break
  else:
    print("Неизвестная команда")
    break

print("До свидания!")

# решение от преподователя - переработать код!!!!
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

