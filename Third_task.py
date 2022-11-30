# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Введите размер массива: '))
my_lst=[]
for i in range(n):
    num=float(input('Введите элемент массива(целое число): '))
    my_lst.append(num)
print(my_lst)
new_lst=[]
for i in range(n):
    new_lst.append(round(my_lst[i] % 1 , 2))
print(new_lst)
max_lst = new_lst[0]
min_lst = new_lst[0]
for i in range(n):
    if new_lst[i] > max_lst:
        max_lst = new_lst[i]
    if new_lst[i] < min_lst:
        min_lst = new_lst[i]      
print(f'Разница между максимальным и минимальным значением дробной части элементов массива: ', {max_lst - min_lst})