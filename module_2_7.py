def print_params(a=1, b='string', c=True):
    print(a, b, c)


values_list = [4, 6.5, 'python']
values_dict = {'a': 'violetta', 'b': 45, 'c': False}
values_list_2 = [None, 7]

print_params()  # Вызов без аргументов
print_params(None)  # Вызов с разным количеством аргументов
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)  # Распаковываем список
print_params(**values_dict)  # Распаковываем словарь
print_params(*values_list_2, 42)  # Проверяем работу второго списка
