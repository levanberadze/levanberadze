# სავარჯიშო 1

x = 15 > 5
print(x)

# სავარჯიშო 3

result = True and not False
print(result)

# სავარჯიშო 4

result = not True or not False
print(result)

# სავარჯიშო 5

result = True and not 0
print(result)

# სავარჯიშო 6

result = 52 < 53.3
print (result)

# სავარჯიშო 7

result = 1 + 52 < 52.3
print(result)

# სავარჯიშო 8

result = 4 != 4.0
print(result)

# სავარჯიშო 2

number = float(input("შეიყვანეთ რიცხვი: "))
if number > 0:
    print("Number is positive")

# სავარჯიშო 3

number = int(input("შეიყვანეთ რიცხვი: "))
if number % 10 == 0:
    print("რიცხვი ბოლოვდება 0-ით")
else:
    print("რიცხვი არ ბოლოვდება 0-ით")

# სავარჯიშო 4

number1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if number1 > 10 and number2 > 10:
    საშუალო = (number1 + number2) / 2
    print(f"ორივე რიცხვი 10-ზე მეტია. მათი საშუალო არითმეტიკული: {საშუალო}")
else:
    ნამრავლი = number1 * number2
    print(f"ორივე რიცხვი 10-ზე ნაკლებია. მათი ნამრავლი: {ნამრავლი}")

# სავარჯიშო 5

number = float(input("შეიყვანეთ რიცხვი: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")
