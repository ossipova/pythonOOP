# Home wokr 2
class Figure:
    unit = 'cm'

    def __init__(self):
        self.perimeter = 0

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * (self.__radius ** 2)

    def info(self):
        print(f"The radius of circle: {self.__radius} {self.unit}, The area of circle: {self.calculate_area()} "
              f"{self.unit}")


circle = Circle(15)
circle.calculate_area()
circle.info()



class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f'Right triangle: side a = {self.__side_a} {self.unit}, side b = {self.__side_b} {self.unit}, '
              f'area = {self.calculate_area()} {self.unit}')


triangle = RightTriangle(8, 9)
triangle.calculate_area()
triangle.info()

figure_list = [Circle(5), Circle(2), RightTriangle(3,4),RightTriangle(5,9),RightTriangle(6,7)]
for figure in figure_list:
    (figure.info())
