import math


def toDict(key, val):
    outdict = {}
    for i in zip(key, val):
        outdict[i[0]] = i[1]
    return outdict


def Exercise_1():
    k = ['a', 'b', 'c']
    v = [35, 20, 10]
    print(toDict(k, v))


def squared(num):
    return num ** 2


def Exercise_2():
    nums = [1, 2, 3, 4]
    out = map(squared, nums)
    print(list(out))


class Polygon():
    def __init__(self, num_sides):
        self.num_sides = num_sides


class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return self.radius * 2 * math.pi


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return (self.length + self.breadth) * 2


def Exercise_3():
    cir = Circle(6)
    print(cir.area())
    print(cir.perimeter())

    rec = Rectangle(6, 6)
    print(rec.area())
    print(rec.perimeter())
    

def Exercise_4():
    a = [1, 3, 5]
    b = [2, 4, 6]
    print(list(map(lambda a, b: a + b, a, b)))


if __name__ == '__main__':
    Exercise_1()
    Exercise_2()
    Exercise_3()
    Exercise_4()
