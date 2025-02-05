students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students: {}'.format(students))
print('students: {}'.format(students[2:4]))
print('students: {}'.format(students[:4]))
print('students: {}'.format(students[2:]))
print('students: {}'.format(students[2:-2]))
print('students: {}'.format(students[-5:-2]))



numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print('numbers: {}'.format(numbers))
print('numbers: {}'.format(numbers[2:4]))
print('numbers: {}'.format(numbers[:4]))
print('numbers: {}'.format(numbers[2:]))
print('numbers: {}'.format(numbers[2:-2]))
print('numbers: {}'.format(numbers[-5:-2]))


str = 'abcdefghijklmnopqrstuvwxyz'
print('str length: {}'.format(len(str)))
print('str: {}'.format(str))
print('str: {}'.format(str[2:4]))
print('str: {}'.format(str[:4]))
print('str: {}'.format(str[2:]))
print('str: {}'.format(str[2:-2]))
print('str: {}'.format(str[-5:-2]))


numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print('numbers: {}'.format(numbers[2:-2]))
print('numbers: {}'.format(numbers[2:-2:2]))
print('numbers: {}'.format(numbers[:-2:2]))
print('numbers: {}'.format(numbers[::2]))



students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students : {}'.format(students))

students[1:4] = ['park chanho', 'lee yonggyu', 'gang hodong']
print('students : {}'.format(students))

students[1:4] = ['박찬호', '이용규']
print('students : {}'.format(students))

students[1:3] = ['park chanho', 'lee yonggyu', 'gang hodong']
print('students : {}'.format(students))




students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students: {}'.format(students))
print('students: {}'.format(students[2:4]))
print('students: {}'.format(students[:4]))
print('students: {}'.format(students[2:]))
print('students: {}'.format(students[2:-2]))
print('students: {}'.format(students[-5:-2]))

print('students: {}'.format(students[slice(2, 4)]))
print('students: {}'.format(students[slice(4)]))
print('students: {}'.format(students[slice(2, len(students))]))
print('students: {}'.format(students[slice(2, len(students)-2)]))
print('students: {}'.format(students[slice(len(students)-5, len(students)-2)]))




