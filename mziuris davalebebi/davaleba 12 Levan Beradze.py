# savarjisho 1

# try:
#     num1 = int(input("shemoiyvane ricxvi: "))
#     num2 = int(input("shemoiyvane ricxvi: "))
#     print(int(num1) / int(num2))
# except ZeroDivisionError:
#     print("0-ze gayofa ar sheidzleba")
# except ValueError:
#     print("funqcia da argumenti araa sheasabamisi")

# savarjisho 2

# def division(num1, num2):
#     try:
#         res = num1 / num2
#         if num1 / num2:
#             return res
#     except ZeroDivisionError:
#         return "0-ze gayofa ar sheidzleba"
#
#
# print(division(10, 20))

# savarjisho 3

# try:
#     x = [1, 2, 3, 4, 5]
#     print(x[0])
# except IndexError:
#     print("indexerror")

# savarjisho 4

# try:
#     with open("myresult.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("faili ar moidzebna")

# savarjisho 5

# try:
#     a = 5
#     b = 10
#     c = -15
#
#     D = (b**2) - (4*a*c)
#     x1 = (-b + (D**0.5)) / (2*a)
#     x2 = (-b - (D**0.5)) / (2*a)
#
#     print(x1, x2)
#
# except ZeroDivisionError:
#     print("0-ze gayofa ar sheidzleba")
# except TypeError:
#     print("error")

# savarjisho 6

# try:
#
#     a = int(input("shemoiyvane ricxvi: "))
#     b = int(input("shemoiyvane ricxvi: "))
#     c = int(input("shemoiyvane ricxvi: "))
#
#     if a + b > c and a + c > b and b + c > a:
#         average = (a + b + c) / 3
#         print(average)
#     else:
#         raise ValueError("samkutxedis gverdebis wess ar etanxmeba")
# except ValueError as m:
#     print(m)
