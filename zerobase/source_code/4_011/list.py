students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))
print('students의 마지막 인덱스 : {}'.format(len(students) - 1))

students.insert(3, '강호동')
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))
print('students의 마지막 인덱스 : {}'.format(len(students) - 1))


words = ['I', 'a', 'boy.']
words.insert(1, 'am')

for word in words:
    print('{} '.format(word), end='')



numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]
inputNumber = int(input('숫자 입력: '))
insertIdx = 0

for idx, number in enumerate(numbers):
    print(idx, number)

    if insertIdx == 0 and inputNumber < number:
        insertIdx = idx

numbers.insert(insertIdx, inputNumber)
print(numbers)