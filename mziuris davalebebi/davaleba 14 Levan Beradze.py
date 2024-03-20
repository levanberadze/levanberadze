# savarjisho 1

# class Fraction:
#     def __init__(self, top, bottom):
#         self.top = top
#         self.bottom = bottom
#
#     def __str__(self):
#         return f"{self.top} / {self.bottom}"
#
#     def inverse(self):
#         return Fraction(self.bottom, self.top)
#
#     def sum(self, sum1):
#         sum1 = self.top + self.bottom
#         return sum1
#
#
# obj1 = Fraction(12, 17)
# obj2 = Fraction(11, 39)
#
# sum_res = obj1.sum(obj2)
# print(sum_res)
# a = obj1.inverse()
# print(a)

# savarjisho 2

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#
# obj1 = Point(1, 2)
# obj2 = Point(10, 20)
#
# distance_obj1 = obj1.distance()
# distance_obj2 = obj2.distance()
#
# print(distance_obj1)
# print(distance_obj2)

# savarjisho 3

# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def distance_between_points(self):
#         return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#
# x1, y1 = input("shemoiyvane ricxvebi x1, y1: ")
# a = x1, y1
#
# x2, y2 = input("shemoiyvane ricxvebi x2, y2: ")
# b = x2, y2
#
# print(a)
# print(b)
