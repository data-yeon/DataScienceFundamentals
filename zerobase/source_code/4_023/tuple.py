students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
sLength = len(students)
print('length of students : {}'.format(sLength))

for i in range(len(students)):
    print('i : {}'.format(i))
    print('students[{}] : {}'.format(i, students[i]))

n = 0
sLength = len(students)
while n < sLength:
    print('n : {}'.format(n))
    print('students[{}] : {}'.format(n, students[n]))
    n += 1


for student in students:
    print('student : {}'.format(student))


myFavoriteSports = ('수영', '배구', '야구', '조깅')

for i in range(len(myFavoriteSports)):
    print('myFavoriteSports[{}]: {}'.format(i, myFavoriteSports[i]))

n = 0
while n < len(myFavoriteSports):
    print('myFavoriteSports[{}]: {}'.format(n, myFavoriteSports[n]))
    n += 1