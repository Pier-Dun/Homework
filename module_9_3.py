first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(fst) - len(snd)) for fst, snd in zip(first, second))
second_result = (bool(len(first[i]) - len(second[i])) for i in range(0, len(first)))
print(list(first_result))
print(list(second_result))