class Figure:
    sides_count = 0
    def __init__(self):
        self.__sides = list()
        self.__color = list()
        self.filled = bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r in range(0, 256) and g in range(0, 256) and b in range(0, 256)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if type(i) != int and i < 0:
                    return False
            return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        elif self.__sides == False:
            self.__sides = [1] * self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__()
        self.__radius = int(*self.get_sides()) / (2 * 3.14)
        self.set_color(*color)
        self.set_sides(*sides)

    def get_square(self):
        return self.__radius * 3.14


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__()
        self.set_color(*color)
        self.set_sides(*sides)

    def get_square(self):
        return ((0.5 * sum(self.get_sides())) * ((0.5 * sum(self.get_sides())) - self.get_sides()[0]) * ((0.5 * sum(self.get_sides())) - self.get_sides()[1]) * ((0.5 * sum(self.get_sides())) - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__()
        if len(sides) == 1:
            sides = sides * 12
        self.set_color(*color)
        self.set_sides(*sides)

    def get_volume(self):
        return int(self.get_sides()[0]) ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((121, 100, 5), 3, 8, 7)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


print('\n------------------------------------' * 2)

# Проверка на изменение цветов:
triangle1.set_color(1,1,1)
print(triangle1.get_color())

# Проверка на изменение сторон:
triangle1.set_sides(5, 3, 4, 4) # Не изменится
print(triangle1.get_sides())

# Проверка площади (треугольника):
print(triangle1.get_square())
