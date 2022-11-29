# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num=int(input('Введите число:'))
binare_num=[]
while num > 0:
    elm=num%2
    binare_num.append(elm)
    num=num//2
binare_num.reverse()
result=0
for i in binare_num:
    result=result*10+i
print(result)
