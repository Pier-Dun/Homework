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

if __name__ == '__main__':

    filenames = [f'Files\\file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = time.time()
    for name in filenames:
        read_info(name)
    end = time.time() - start
    print(end)

    # Многопроцессный
    start = time.time()
    with Pool(processes=4) as p:
        p.map(read_info, filenames)
    end = time.time() - start
    print(end)
