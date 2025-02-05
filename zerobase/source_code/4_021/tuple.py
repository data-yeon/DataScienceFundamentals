students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

print('students[0]: {}'.format(students[0]))
print('students[1]: {}'.format(students[1]))
print('students[2]: {}'.format(students[2]))
print('students[3]: {}'.format(students[3]))
print('students[4]: {}'.format(students[4]))

# print('students[5]: {}'.format(students[5]))


numbers = (10, 20, 30, 40, 50, 60, 70)

print('numbers[0]: {}'.format(numbers[0]))
print('numbers[1]: {}'.format(numbers[1]))
print('numbers[2]: {}'.format(numbers[2]))
print('numbers[3]: {}'.format(numbers[3]))
print('numbers[4]: {}'.format(numbers[4]))
print('numbers[5]: {}'.format(numbers[5]))
print('numbers[6]: {}'.format(numbers[6]))

# print('numbers[7]: {}'.format(numbers[7]))

strs = (3.14, '십', 20, 'one', '3.141592')

print('strs[0]: {}'.format(strs[0]))
print('strs[1]: {}'.format(strs[1]))
print('strs[2]: {}'.format(strs[2]))
print('strs[3]: {}'.format(strs[3]))
print('strs[4]: {}'.format(strs[4]))

# print('strs[5]: {}'.format(strs[5]))


datas = (10, 20, 30, (40, 50, 60))

print('datas[0]: {}'.format(datas[0]))
print('datas[1]: {}'.format(datas[1]))
print('datas[2]: {}'.format(datas[2]))
print('datas[3]: {}'.format(datas[3]))

print('datas[3][0]: {}'.format(datas[3][0]))
print('datas[3][1]: {}'.format(datas[3][1]))
print('datas[3][2]: {}'.format(datas[3][2]))



students = ('김성예', '신경도', '박기준', '최승철', '황동석')
print('-- 인덱스가 짝수인 학생 --')
print('students[0] : {}'.format(students[0]))
print('students[2] : {}'.format(students[2]))
print('students[4] : {}'.format(students[4]))
print('-- 인덱스가 홀수인 학생 --')
print('students[1] : {}'.format(students[1]))
print('students[3] : {}'.format(students[3]))


for i in range(5):
    if i % 2 ==0:
        print('인덱스 짝수 : students[{}] : {}'.format(i, students[i]))
    else:
        print('인덱스 홀수 : students[{}] : {}'.format(i, students[i]))



