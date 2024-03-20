# # savarjisho 1
#
# students = {
#     "Alice": {"Math": 85, "Science": 90},
#     "Bob": {"Math": 75, "History": 80}
# }
#
#
# def add_student(students, name, grades):
#     students[name] = grades
#     name = input("Enter the student's name: ")
#
#
# def update_grade(students, name, subject, grade):
#     pass
#
#
# def calculate_average(students, name):
#     if name in students:
#         points = students[name].values()
#         average = sum(points) / len(points)
#         return average
#
#
# def display_student(students, name):
#     pass
#
#
#
# print("Options:")
# print("1. Add Student")
# print("2. Update Grade")
# print("3. Display Student Information")
# print("4. Calculate Average Grade")
# print("5. Exit")
# choice = input("Enter your choice: ")

# savarjisho 2

# person = {
#     "name": "Levan",
#     "age": 15,
#     "city": "Tbilisi",
#     "occupation": "student"
# }
# print(person)

# savarjisho 3

# person = {
#     "name": "Levan",
#     "age": 15,
#     "city": "Tbilisi",
#     "hobby": "ჭამა და ძილი"
# }
# print(person)

# savarjisho 4

# def merge_dictionaries(dict1, dict2):
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict
#
# dict1 = {"name1": "Levan", "age1": 15}
# dict2 = {"name2": "Dato", "age2": 16}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)

# savarjisho 5

# def filter_dictionary(dict):
#     dict1 = {}
#     for key, value in dict.items():
#         if value > 10:
#             dict1[key] = value
#     return dict1
#
#
# dict2 = {"first": 25, "second": 5, "third": 10, "fourth": 20}
# filtered_dict = filter_dictionary(dict2)
# print(filtered_dict)

# savarjisho 6

# sia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# dict = {num: num**3 for num in sia}
# print(dict)

# savarjisho 7

# def frequency_counter(list1):
#     dict = {}
#     for item in list1:
#         if item in dict:
#             dict[item] += 1
#         else:
#             dict[item] = 1
#     return dict
#
# list = [312, 2141, 52, 15, 5, 7, 15]
# res = frequency_counter(list)
# print(res)

# savarjisho 8

# def invert_dictionary(dict):
#
#                           es ver gavige

# savarisho 9 (bonusi)

# def create_dictionary(list1, list2):
#     if len(list1) != len(list2):
#         return "ლისტების სიგრძე უნდა ემთხვეოდეს"
#
#     dict = {}
#     for i in range(len(list1)):
#         dict[list1[i]] = list2[i]
#     return dict
#
#
# list1 = ["Levani", "Nika", "Gio"]
# list2 = [15, 16, 17]
# res = create_dictionary(list1, list2)
# print(res)
