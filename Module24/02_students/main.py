from statistics import mean
import random


class Student:
    def __init__(self, name, group, mark):
        self.FirstSecondName = name
        self.GroupNumber = group
        self.Performance = mark


def sort(list):
    N = len(list) - 1
    for j in range(N):
        F = 0
        for i in range(N - j):
            if mean(list[i].Performance) > mean(list[i + 1].Performance):
                list[i], list[i + 1] = list[i + 1], list[i]
                F += 1

        if F == 0:
            break


students = []

for i in range(10):
    # f_s_name = input("First Second Name: ")
    # group_number = input("Group Number: ")
    f_s_name = str(i + 1)
    group_number = str(i + 1)
    marks = []
    for j in range(5):
        marks.append(random.randint(1, 5))
        # marks.append(input(f"{j + 1} mark: "))

    student = Student(f_s_name, group_number, marks)
    students.append(student)
    print(f"{student.FirstSecondName} - {student.GroupNumber} - {student.Performance}")
    print("")

sort(students)

for i in range(len(students)):
    student = students[i]
    print(f"{student.FirstSecondName} - {student.GroupNumber} - {student.Performance}")

# зачтено
