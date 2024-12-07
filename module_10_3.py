import random
import threading
import time


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rnd = int(random.choice(range(50, 500)))
            self.balance += rnd
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {rnd}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rnd = int(random.choice(range(50, 500)))
            print(f'Запрос на {rnd}')
            if rnd <= self.balance:
                self.balance -= rnd
                print(f'Снятие: {rnd}, Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')