students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('students: {}'.format(students))

searchCnt = students.count('홍길동')
print('searchCnt: {}'.format(searchCnt))

searchCnt = students.count('강호동')
print('searchCnt: {}'.format(searchCnt))

searchCnt = students.count('김아무개')
print('searchCnt: {}'.format(searchCnt))




students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('students: {}'.format(students))

del students[1]
print('students: {}'.format(students))

del students[1:4]
print('students: {}'.format(students))

del students[2:]
print('students: {}'.format(students))




import random

types = ['A', 'B', 'AB', 'O']
todayData = []
typeCnt = []

for i in range(100):
    type = types[random.randrange(len(types))]
    todayData.append(type)

print('todayData : {}'.format(todayData))
print('todayData length : {}'.format(len(todayData)))

for type in types:
    print('{}형 \t : {}개'.format(type, todayData.count(type)))




while True:
    if todayData.count('O') > 0:
        todayData.remove('O')
    else:
        break;

print('todayData : {}'.format(todayData))
print('todayData length : {}'.format(len(todayData)))

for type in types:
    print('{}형 \t : {}개'.format(type, todayData.count(type)))


