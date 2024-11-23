import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda fst, snd: fst == snd, first, second)))

print('\n-------------------\n-------------------')

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as opnd_file:
            for i in data_set:
                opnd_file.write(f'{i}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print('\n-------------------\n-------------------')

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())