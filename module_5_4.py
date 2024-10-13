class House:

    houses_history = [] # модуль_5_4

    def __new__(cls, *args, **kwargs): # модуль_5_4
        House.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self): # модуль_5_2
        return self.number_of_floors

    def __str__(self): # модуль_5_2
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other): # модуль_5_3
        return self.number_of_floors == other

    def __lt__(self, other): # модуль_5_3
        return self.number_of_floors < other

    def __le__(self, other): # модуль_5_3
        return self.number_of_floors <= other

    def __gt__(self, other): # модуль_5_3
        return self.number_of_floors > other

    def __ge__(self, other): # модуль_5_3
        return self.number_of_floors >= other

    def __ne__(self, other): # модуль_5_3
        return self.number_of_floors != other

    def __add__(self, value): # модуль_5_3
        self.number_of_floors += value
        return self

    def __radd__(self, value): # модуль_5_3
        return self.__add__(value)

    def __iadd__(self, value): # модуль_5_3
        return self.__add__(value)

    def __del__(self): # модуль_5_4
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)