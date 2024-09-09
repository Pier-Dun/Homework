immutable_var = 1, True, 'hi'
print(immutable_var)
# immutable_var[1] = False  Кортеж не поддерживает изменение, добавление и удаление объектов, как списки
mutable_list = [1, True, 'hi']
mutable_list[1] = False
print(mutable_list)