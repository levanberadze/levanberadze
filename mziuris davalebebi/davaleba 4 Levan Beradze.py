# savarjisho 1
#
# number = int(input("shemoiyvanet ricxvi: "))
#
# for x in range(1, number + 1):
#     if number % x == 0:
#         print(x)

# savarjisho 2
#
# number1 = int(input("shemoiyvanet ricxvi1: "))
# number2 = int(input("shemoiyvanet ricxvi2: "))
#
# for x in range(1, (number1 * number2) + 1):
#     if number1 % x == 0 and number2 % x == 0:
#         print(x)

# savarjisho 3

# number1 = int(input("shemoiyvanet mteli dadebiti ricxvi1: "))
# number2 = int(input("shemoiyvanet mteli dadebiti ricxvi2: "))
#
# for x in range(1, min(number1, number2) + 1):
#     if number1 % x == 0 and number2 % x == 0:
#         gcd = x
# print(f"The greatest common divisor of {number1} and {number2} is: {gcd}")

# savarjisho 4

# number1 = int(input("shemoiyvanet mteli dadebiti ricxvi1: "))
# number2 = int(input("shemoiyvanet mteli dadebiti ricxvi2: "))
#
# a = max(number1, number2)
#
# while True:
#     if a % number1 == 0 and a % number2 == 0:
#         lcm = a
#meti vegar gavagrdzele ver gavige es savarjisho

# savarjisho 5

greatest_odd = float("-inf")

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))

    if number % 2 != 0 and number > greatest_odd:
        greatest_odd = number

if greatest_odd != float("-inf"):
    print(f"The greatest odd number is: {greatest_odd}")
else:
    print("sheyvanili ricxvebidan kenti ar yofila arcerti")


