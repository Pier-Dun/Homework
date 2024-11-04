def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    number_of_string = 1
    strings_positions = {}
    for i in strings:
        strings_positions[(number_of_string, file.tell())] = i
        file.write(f'{i}\n')
        number_of_string += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
