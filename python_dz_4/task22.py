# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# Например:
# 11 6 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

list_1 = []
list_2 = []

for i in range(int(input("Введите количество элементов первого множества: "))):
    list_1.append(int(input(f"Введите {i + 1}-й элемент первого множества: ")))

for i in range(int(input("Введите количество элементов второго множества: "))):
    list_2.append(int(input(f"Введите {i + 1}-й элемент второго множества: ")))

list_3 = set()

for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_2[j] == list_1[i]:
            list_3.add(list_1[i])

list_3 = list(list_3)

for i in range(len(list_3)):
    for j in range(i + 1, len(list_3)):
        if list_3[j] < list_3[i]:
            temp = list_3[i]
            list_3[i] = list_3[j]
            list_3[j] = temp

print(list_3)

###

# num_1 = int(input("Введите количество элементов первого множества: "))
# set_1 = set([int(input(f"Введите {i + 1}-й элемент первого множества: ")) for i in range(num_1)])
#
# num_2 = int(input("Введите количество элементов второго множества: "))
# set_2 = set([int(input(f"Введите {i + 1}-й элемент второго множества: ")) for i in range(num_2)])
#
# result = list(set_1.intersection(set_2))
# result.sort()
# print(result)
