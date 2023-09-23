# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

str_1 = 'a a a b c a a d c d d'
str_1 = str_1.split()  # ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']

print(str_1)

my_dict = {}
result = ''

for i in str_1:
    if i not in my_dict:
        my_dict[i] = 0  # {'a': 0}
        result += f'{i} '
    else:
        my_dict[i] += 1  # {'a': 1}
        result += f'{i}_{my_dict[i]} '
print(result)
