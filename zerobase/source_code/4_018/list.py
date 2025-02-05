students = ['홍길동', '박찬호', '이용규']
print('students: {}'.format(students))

studentsMul = students * 2
print('studentsMul: {}'.format(studentsMul))

numbers = [2, 50, 0.12, 1, 9]
print('numbers: {}'.format(numbers))

numbersMul = numbers * 3
print('numbersMul: {}'.format(numbersMul))




students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('students: {}'.format(students))

searchIdx = students.index('강호동')
print('searchIdx: {}'.format(searchIdx))

searchIdx = students.index('강호동', 2, 6)
print('searchIdx: {}'.format(searchIdx))

numbers = [2, 50, 0.12, 1, 9, 7, 17, 0.12, 100, 3.14]
print('numbers: {}'.format(numbers))

searchIdx = numbers.index(0.12)
print('searchIdx: {}'.format(searchIdx))

searchIdx = numbers.index(0.12, 3)
print('searchIdx: {}'.format(searchIdx))

str = '홍길동강호동박찬호이용규박승철강호동김지은'
searchIdx = str.index('강호동')
print('searchIdx: {}'.format(searchIdx))

searchIdx = str.index('강호동', 10, 20)
print('searchIdx: {}'.format(searchIdx))

searchIdx = str.index('ㅎㅎ')
print('searchIdx: {}'.format(searchIdx))





import random

sampleList = random.sample(range(1, 11), 10)

selectIdx = int(input('숫자 7의 위치 입력: '))
searchIdx = sampleList.index(7)

if searchIdx == selectIdx:
    print('빙고!!')
else:
    print('ㅜㅜ')

print('sampleList: {}'.format(sampleList))
print('searchIdx: {}'.format(searchIdx))



