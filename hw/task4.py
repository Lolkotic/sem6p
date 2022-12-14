from memory_profiler import profile

@profile

#При стандартном способе затраты памяти - 22.0 MiB
def task1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


print(task1(int(input('Введите делимое: ')), int(input('Введите делитель: '))))


#При использовании лямбда-функции затраты памяти : 0.0 MiB
def task1(a, b):
    f = lambda a,b: a / b
    print(f)
print(task1(int(input('Введите делимое: ')), int(input('Введите делитель: '))))


