print('Делаем новый тест!')
print('Как думаете, сколько раз можно поделить 1 на 2?')

number = 1
count = 0
save_number = number
while number != 0:
  save_number = number
  number /= 2
  count += 1
print('Привет! Это маленькая тестовая программа!')
print('Самое маленькое возможное число путем постоянного деления числа 1 на 2:', save_number)
print('Количесвто делений на 2:', count)
print('Ура, программа закончилась!')
