"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""


class Rectangle:
    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh

    def area(self):
        return self.width * self.heigh

    def perimeter(self):
        return 2 * (self.width + self.heigh)

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        width = diagonal / (1 + aspect_ratio ** 2) ** (1 / 2)
        heigh = aspect_ratio * width
        return cls(width, heigh)

    @staticmethod
    def is_square(width, height):
        if width == height:
            return True
        else:
            return False


rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
