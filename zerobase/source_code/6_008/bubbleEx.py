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
sortedStudents = sm.bubbleSort(students) # 얕은 복사  (똑같은 객체에다가 이용하고있는것이다.)
# 만약 원본 데이터를 유지하고, 새로운 데이터를 만들고 싶다면,
print(f'students: {students}')
print(f'sortedStudents: {sortedStudents}')
