import math


class Figure:
    sides_count = 0

    def __init__(self, color=(255, 255, 255), *sides):
        self.__color = list(color)
        self.filled = False
        self.__sides = [1] * self.sides_count
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
            0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(255, 255, 255), radius=1):
        super().__init__(color)
        self.set_sides(2 * math.pi * radius)

    def get_square(self):
        return math.pi * (self.get_sides()[0] / (2 * math.pi)) ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(255, 255, 255), length=1):
        super().__init__(color)
        self.set_sides(length, length, length, length, length, length,
                       length, length, length, length, length, length)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], (int, float)):
            self.__sides = [new_sides[0]] * self.sides_count


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)


    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))

    print(cube1.get_volume())