m = list([])
n = int(input('Введите количество критериев: '))
for i in range(n):  # Создаем двумерный массив
    m.append([])
    for j in range(n):
        m[i].append(0)

for i in range(len(m)):
    for j in range(len(m)):
        if i < j:
            m[i][j] = float(input(f'Введите важность критерий {i + 1} относительно {j + 1} ')) # Заполняем массив коэффициентами
            m[j][i] = 1 / float(m[i][j])
        elif i == j:
            m[i][j] = 1

sum_line = []
for i in range(len(m)):
    k = 0
    for j in range(len(m)):
        k += float((m[i][j]))
    sum_line.append(k) # Заполняем новый массив суммой строк массива с коэффициентами

full_sum = 0
for i in sum_line: # Находим сумму элементов нового массива
    full_sum += i

kriter = []
for i in sum_line: # Заполняем еще один новый массив весом критерия
    kriter.append(i / full_sum)

for i in range(len(kriter)): # Выводим вес каждого критерия
    print(f'Вес критерия №{i + 1} - {kriter[i]}')
