import sortMod as sm
import random as rd

students = []

for i in range(20):
    students.append(rd.randint(170, 185))

print(f'students: {students}')
print(f'students length: {len(students)}')

# 얕은 복사
# sortedStudents = sm.bubbleSort(students, deepCopy=False)
# print(f'students: {students}')
# print(f'sortedStudents: {sortedStudents}')

# 깊은 복사
sortedStudents = sm.bubbleSort(students)
print(f'students: {students}')
print(f'sortedStudents: {sortedStudents}')
