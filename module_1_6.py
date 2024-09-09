# Работа со словарями
my_dict = {'Dima': 2000, 'Nastya':2002}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Sasha', 'Такого ключа нет'))
my_dict.update({'Vlad': 1997,
                'Lera': 2001})
a = my_dict.pop('Lera')
print(a)
print(my_dict)

# Работа со множествами
my_set = {2, 1, 1 < 2, True, 'Waffles', True, 7, 19.9}
print(my_set)
my_set.update({'19.9',
               False})
my_set.remove('19.9')
print(my_set)