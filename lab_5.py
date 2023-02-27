# #1
# mylist=["Almaty","Astana","Aqtau","Taldyqorgan","Aktobe"]
# mylist.append("Semey")
# print("method append:",mylist)
# mylist.insert(3,"Zhezqazgan")
# print("method insert:",mylist)
# mylist.remove("Aqtau")
# print("method remove:",mylist)
# mylist.pop(4)
# print("method pop:",mylist)
# mylist.reverse()
# print("method reverse:",mylist)
# #resume
# last_name = "Samet"
# first_name = "Aibek"
# age = 20
# country = "Kazakhstan"
# specialization = "IT programmer"
# list = [last_name,first_name,age,country]
# list.append(specialization)
# print(list)
#1-ESEP
# groups = {}
# num_students = int(input("Enter number of students: "))
# for i in range(num_students):
#     name = input("Enter name:")
#     group = input("Enter group ")
#     if group not in groups:
#         groups[group] = []
#     groups[group].append(name)
# for group, students in sorted(groups.items()):
#     print(group + ":")
#     for student in sorted(students):
#         print("  " + student)
#2-ESEP
# grades = {
#     "Sametov": {"Functional": 5, "English": 4, "Algorithms": 5},
#     "Bekzhanov": {"Functional": 4, "English": 5, "Algorithms": 5},
#     "Sagatov": {"Functional": 5, "English": 5, "Algorithms": 4}
# }

# def get_grades(student_name):
#     if student_name in grades:
#         return grades[student_name]
#     else:
#         return None

# student_name = input("Enter last name: ")
# student_grades = get_grades(student_name)
# if student_grades is not None:
#     print(f"Marks {student_name}:")
#     for subject, grade in student_grades.items():
#         print(f"{subject}: {grade}")
# else:
#     print("Student not found")
#3-4 esep
# numbers = []
# while True:
#     number = int(input("Enter numbers: "))
#     if number == 0:
#         break
#     numbers.append(number)
# numbers_sorted = sorted(numbers)
# print("Osu retimen:")
# for number in numbers_sorted:
#     print(number)

# numbers_sorted = sorted(numbers, reverse=True)
# print("Kemu retimen:")
# for number in numbers_sorted:
#     print(number)
#5-esep
# import random
# ticket_numbers = random.sample(range(1, 50), 6)
# ticket_numbers.sort()
# print("Number of tickets:")
# for number in ticket_numbers:
#     print(number)
#6-esep
# def is_sorted(lst):
#     if lst == sorted(lst):
#         return True
#     elif lst == sorted(lst, reverse=True):
#         return True
#     else:
#         return False
# lst = list(map(int, input("Enter numbers of list: ").split()))
# if is_sorted(lst):
#     print("List is sorted")
# else:
#     print("List is not sorted")

