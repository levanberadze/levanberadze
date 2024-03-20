# savarjisho 1

# f = "cudi_file.txt"
#
# with open(f, "w") as f:
#     f.write("gamarjoba me mqvia gela")
# print(f)
# f.close()

# savarjisho 2

# f = "cudi_file.txt"
#
# f = open(f, "r")
# content = f.read()
# print(content)
# symbol_count = len(content)
# print(symbol_count)
# f.close()

# savarjisho 3

# f = "cudi_file.txt"
#
# append_text = "\ngamarjoba me mqvia gocha"
# f = open(f, "a")
# f.write(append_text)
# f.close()

# savarjisho 4

# f_path = "cudi_file.txt"
# f1_path = "axali_file.txt"
#
# f = open(f_path, "r")
# content = f.read()
# f.close()
#
# f1 = open(f1_path, "w")
# f1.write(content)
# f1.close()

# savarjisho 5

# f1_path = "cudi_file.txt"
# f2_path = "axali_file.txt"
# f3_path = "dzveli_file.txt"
#
# f1 = open(f1_path, "r")
# content1 = f1.read()
# f1.close()
#
# f2 = open(f2_path, "r")
# content2 = f2.read()
# f2.close()
#
# f3_content = content1 + content2
#
# f3 = open(f3_path, "w")
# f3.write(f3_content)
# f3.close()

# savarjisho 6

# f_path = "cudi_file.txt"
#
# f = open(f_path, "r")
# content = f.read()
# print(content.upper())
# f.close()

# savarjisho 7

# with open("data.txt", "w") as f:
#     while True:
#         input_from_user = input("sheiyvane 0 tu ginda rom dasruldes: ")
#         if input_from_user == "0":
#             break
#         f.write(input_from_user)

# savarjisho 8

f_path = "cudi_file.txt"
f1_path = "axali_file.txt"

f = open(f_path, "r")
content = f.read()
print(content.split())
a = content.split()
b = " ".join(a)
print(b)
f.close()

f1 = open(f1_path, "w")
f1.write(content)
f1.close()


