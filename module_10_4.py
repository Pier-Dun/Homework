import random
import time
from queue import Queue
from threading import Thread


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.choice(range(3, 11)))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
                elif table == self.tables[-1]:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(i.guest for i in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
