from math import pi


def rounded(f): return lambda x: round(f(x), 2)

class Parameters:

    def __init__(self, par):
        self.par = par

    def choose_figure(self, figure):
        self.figure = figure

    @rounded
    def area(self):
        return self.figure.area(self.par)

    @rounded
    def perimeter(self):
        return self.figure.perimeter(self.par)

    @rounded
    def volume(self):
        return self.figure.volume(self.par)

class RegularPoly:
    def perimeter(self, par):
        return self.nsides * par

    def area(self, par):
        return par ** 2 * self.phi

    volume = lambda *_: 0


class Circle(RegularPoly): nsides, phi = pi * 2, pi

class Triangle(RegularPoly): nsides, phi = 3, 0.43301

class Square(RegularPoly): nsides, phi = 4, 1

class Pentagon(RegularPoly): nsides, phi = 5, 1.72048

class Hexagon(RegularPoly): nsides, phi = 6, 2.598076211

class Cube(RegularPoly): nsides, phi, volume = 12, 6, 3..__rpow__