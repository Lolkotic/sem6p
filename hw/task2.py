

# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


from timeit import timeit

#Используем while и for, время выполнения - 2.35. Число постоянно больше,
# поэтому возможно while немного замедляет работу
element_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)


#Используем for, время выполнения - 2.13
n = int(input("Введите количество элементов в Вашем списке: "))
matrix = []
for i in range(n):
    matrix.append(input(f"Введите элемент # {i+1}: "))
print(f"Ваш список: {matrix}")
for j in range(0, (len(matrix)-1),2):
    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
print(f"Измененный список: {matrix}")


print(timeit("my_list", globals=globals(), number=1000))
print(timeit("matrix", globals=globals(), number=1000))