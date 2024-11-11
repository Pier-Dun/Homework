import os, time

for root, dirs, files in os.walk('Pong_game'):
    print(root)
    print(dirs)
    print(files)
    for file in files:
        filepath = os.path.join(os.path.dirname(f'{root}\\{dirs}'), file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname('game.py')
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')