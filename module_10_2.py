import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self):
        hp = 100
        start = time.time()
        while hp > 0:
            time.sleep(1)
            hp -= self.power
            end = time.time()
            if (end - start) > 1:
                print(f'{self.name} сражается {round(end - start)} день(дня)..., осталось {hp} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        start = time.time()
        self.battle()
        end = time.time()
        print(f'{self.name} одержал победу спустя {round(end - start)} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')