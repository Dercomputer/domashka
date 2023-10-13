"""

x = input()
y = input()
while len(x) != 0 or len(y) != 0:
    if len(x) == len(y): 
        a, b = str(int(x) // 10 ** (len(x)-1)), str(int(y) // 10 ** (len(y)-1))
        if a == b:
            print("YES")
        elif a > b:
            print("YES")
        elif a < b:
            print("No")
    x, y = x[1:], y[1:]
x = input()
y = input()
while x != 0 or y != 0:
    print(x,y)
    x, y = x[1:], y[1:]
    break

    
a = input()
lst= []
while a:
    lst.append(a)
    a = input()
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        a, b = str(i), str(j)
        if str(int(i) // 10 ** (len(a)-1)) == str(int(j) // 10 ** (len(b)-1)):
            print("YES")
        else:
            print(str(int(i) // 10 ** (len(a)-1)), str(int(j) // 10 ** (len(b)-1)))

            
a = input()
lst= []
while a:
    lst.append(a)
    a = input()

lst.sort(key=lambda x: x[2])
print(lst)

a = input()
lst= []
while a:
    lst.append(a)
    a = input()
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        i, j = str(i), str(j)
        while len(i) != 0 or len(j) != 0:
            if len(i) == len(j): 
                a, b = str(int(i) // 10 ** (len(i)-1)), str(int(j) // 10 ** (len(j)-1))
                if a == b:
                    print("YES")
                elif a > b:
                    print("YES")
                elif a < b:
                    print("No")
            i, j = i[1:], j[1:]

def compare(str1, str2):
    return int(str1+str2) - int(str2+str1)


a = input()
lst= []
while a:
    lst.append(a)
    a = input()
print(lst)

lst.sort(reverse=True, key=compare)
result = ''.join(lst)
maxnumber = (a)
print(maxnumber)

def compare(str1, str2):
    # Сравнение строк-комбинаций чисел
    return int(str1 + str2) - int(str2 + str1)

def find_max_number(numbers):
    # Преобразование чисел в строки
    numbers = [str(num) for num in numbers]

    # Сортировка чисел по убыванию
    numbers.sort(reverse=True, key=lambda x: compare(str(x), str2=''))

    # Склеивание чисел в одну строку
    result = ''.join(numbers)

    # Преобразование строки в число
    result = int(result)

    return result

# Создание пустого списка
numbers = []

# Цикл для периодического ввода данных пользователем
while True:
    num = input("Введите число (или 'q' для завершения): ")
    # Проверка на выход из цикла
    if num.lower() == '':
        break
    # Преобразование строки в целое число и добавление в список
    numbers.append(int(num))

max_number = find_max_number(numbers)
print(max_number)  # Вывод максимально возможного числа
4444444444444444444444
def maxnumber(numbers):
    numbers.sort(key=lambda x: x * 3, reverse=True)
    result = ''.join(numbers)
    result = int(result)
    return result

numbers = []
while True:
    number = input("Введите число: ")
    if number == '':
        break
    numbers.append((number))

max_number = maxnumber(numbers)
print(max_number)
4444444444444444444444
"""
x = input()
y = input()
if x * 3 > y:
    print("YES")
elif x * 3 < y:
    print("NO")
else:
    print("XZ")