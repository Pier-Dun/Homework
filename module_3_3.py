# функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Проверка вызовов
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров
values_list = [4, 'Egor', [False]]
values_dict = {'a': 2, 'b': 'string', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [True, 'Vladimir']
print_params(*values_list_2, 42)
