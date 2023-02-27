#1-esep
# import random
# def generate_tuple(start, end, size):
#     return tuple(random.randint(start, end) for _ in range(size))
# t1 = generate_tuple(0, 5, 10)
# t2 = generate_tuple(-5, 0, 10)
# t3 = t1 + t2
# count_zeros = t3.count(0)
# print("t1:", t1)
# print("t2:", t2)
# print("t3:", t3)
# print("Count of zeros in t3:", count_zeros)
# #2-esep
# matryoshka = (34, (32.15, (3+25j, ('Aibek', ()))) )
# print(matryoshka[1][1][1][0] + ' ' + str(matryoshka[0]))
#3-esep
# expenses = []
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for day in days:
#     daily_expenses = {}
#     print("Enter expenses for", day)
#     daily_expenses["Transportation"] = float(input("Transportation: "))
#     daily_expenses["Food"] = float(input("Food: "))
#     daily_expenses["Entertainment"] = float(input("Entertainment: "))
#     expenses.append(daily_expenses)
# total_expenses = 0
# for daily_expenses in expenses:
#     for category, expense in daily_expenses.items():
#         total_expenses += expense
# print("Total expenses for the week:", total_expenses," KZT")
#4-esep
# names_str = input("Enter name of students: ")
# names_tuple = tuple(names_str.split())
# for name in names_tuple:
#     if "va"  in name:
#         print(name, end=" ")
#5-esep
from transliterate import translit

text = input("Введите текст на казахском языке: ")
transliterated_text = translit(text, "kk", reversed=True)
print(transliterated_text)


