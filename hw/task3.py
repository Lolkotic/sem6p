from memory_profiler import profile

@profile
#При решении функцией время  - 21.7 MiB
def int_func(word):
    return word.capitalize()
text = input('Введите строку из слов, разделенных пробелами: ')
print(' '.join([int_func(word) for word in text.split()]))

# при решении встроенным методом не пишет про использование памяти
s = input('Введите строку из слов: ')
print(s.title())
