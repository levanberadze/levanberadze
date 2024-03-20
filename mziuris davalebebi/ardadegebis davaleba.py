# savarjisho 1

# def get_count(sentence):
#     count = 0
#     vowels = "a", "e", "i", "o", "u"
#     for letter in sentence:
#         if letter in vowels:
#             count += 1
#     return count
#
# sentence = "skola ar minda"
# res = get_count(sentence)
# print(res)

# savarjisho 2

# def disemvowel(string_):
#     res = ""
#     for i in string_:
#         if i in "aeiouAEIOU":
#             continue
#         else:
#             res += i
#     return res
#
# sentence = "This website is for losers LOL!"
# res = disemvowel(sentence)
# print(res)

# savarjisho 3

# def square_digits(num):
#     res = ""
#     num = str(num)
#     for i in num:
#         res += str(int(i) ** 2)
#     return int(res)
# concatenated_number = square_digits(9119)
# print(concatenated_number)

# savarjisho 5

# def positive_sum(arr):
#     res = 0
#     for num in arr:
#         if num > 0:
#             res += num
#     return res
#
# arr = (1, 2, 15, -17, 7)
# res = positive_sum(arr)
# print(res)

# savarjisho 6

# def get_middle(s):
#     my_len = len(s)
#     if my_len % 2 == 0:
#         return s[int(my_len / 2 - 1): int(my_len / 2 + 1)]
#     else:
#         return s[int(my_len / 2)]

# savarjisho 7
#
# def filter_list(l):
#     new_list = []
#     for i in l:
#         if type(i) == int:
#             new_list.append(i)
#     return new_list

# savarjisho 9

# def solution(string):
#     reversed_str = ''.join(reversed(string))
#     return reversed_str

# def solution(string):
#     return string[::-1]

# savarjisho 10

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"