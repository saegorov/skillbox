import random

def mainMenu(): # Главное меню
  print('\nДобро пожаловать!')
  print('Я новая программа и я хотела бы поиграть с Вами в игру!')
  choice = int(input('Выберите в какую игру хотите сыграть с компьютером: \n1. "Камень, ножницы, бумага" \n2. "Угадай число" \n3. Выход \nВыбор: '))
  if choice == 1:
    rock_paper_scissors()
  elif choice == 2:
    guess_the_number()
  elif choice == 3:
    print('\nДо свидания! ')
  else:
    print('Ошибка ввода. Необходимо ввести цифру 1 или 2.')
    mainMenu()

def loop_RPS():
  choice = input('\nХочешь сыграть в игру еще раз? ')
  if choice == 'Да' or choice == 'да':
    rock_paper_scissors()
  else:
    mainMenu()
def loop_GtN():
  choice = input('\nХочешь сыграть еще раз? ')
  if choice == 'Да' or choice == 'да':
    guess_the_number()
  else:
    mainMenu()

def rock_paper_scissors(): #"Камень, ножницы, бумага"
  print('\nПривет! \nСыграем в игру "Камень, ножницы, бумага"!')
  comp_choice = random.randint(1, 3)
  user_choice = int(input('Введите что вы выбираете \n1. Камень \n2. Ножницы \n3. Бумага \nВаш выбор: '))
  if user_choice == 1:
    if comp_choice == 1:
      print('Результат: Ничья')
      loop_RPS()
    if comp_choice == 2:
      print('Результат: Вы победили! :) Компьютер проиграл!')
      loop_RPS()
    else:
      print('Вы проиграли! :( Компьютер победил!')
      loop_RPS()
  elif user_choice == 2:
    if comp_choice == 1:
      print('Вы проиграли! :( Компьютер победил!')
      loop_RPS()
    if comp_choice == 2:
      print('Результат: Ничья')
      loop_RPS()
    else:
      print('Результат: Вы победили! :) Компьютер проиграл!')
      loop_RPS()
  elif user_choice == 3:
    if comp_choice == 1:
      print('Результат: Вы победили! :) Компьютер проиграл!')
      loop_RPS()
    if comp_choice == 2:
      print('Вы проиграли! :( Компьютер победил!')
      loop_RPS()
    else:
      print('Результат: Ничья')
      loop_RPS()
  else:
    print('Ошибка ввода. Введите значение 1, 2 или 3.')
    rock_paper_scissors()

def guess_the_number(): #"Угадай число"
  print('\nПривет! \nДавай сыграем в игру "Угадай число"!')
  print('Я загадаю число от 1 до 100. \nУ тебя есть 7 попыток, чтобы его угадать!')
  comp_num = random.randint(1, 100)
  check = False
  for i in range(7):
    print('\nОсталось попыток:', 7 - i)
    user_num = int(input('Введите число: '))
    if user_num > comp_num:
      print('\nЗагаданное число меньше')
    elif user_num < comp_num:
      print('\nЗагаданное число больше')
    else:
      check = True
      print('\nМолодец! Ты угадал!')
      break
  if check == False:
    print(f'Ты был близок, но не получилось. \nЯ загадал число {comp_num}')
  loop_GtN()

mainMenu() 
