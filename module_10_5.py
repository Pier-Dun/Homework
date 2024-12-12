import multiprocessing
from multiprocessing import Pool
import time


def read_info(name):
    all_data =[]
    with open(name, 'r', encoding='UTF-8') as file:
        for line in file:
            if line:
                all_data.append(line)
            else:
                break
    return all_data



filenames = [f'Files\\file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = time.time()
for name in filenames:
    read_info(name)
end = time.time()
print(end - start)

# Многопроцессный
if __name__ == '__main__':
    start = time.time()
    with Pool(4) as p:
        map(read_info, filenames)
    end = time.time()
    print(end - start)