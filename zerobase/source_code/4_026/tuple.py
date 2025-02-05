students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students: {}'.format(students))

# 아이템 추가
students.append('강호동')
print('students: {}'.format(students))

# 아이템 변경
students[3] = '유재석'
print('students: {}'.format(students))

# 아이템 삭제
students.pop()
print('students: {}'.format(students))




students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print('students: {}'.format(students))

# 아이템 추가
students.append('강호동')
print('students: {}'.format(students))

# 아이템 변경
students[3] = '유재석'
print('students: {}'.format(students))

# 아이템 삭제
students.pop()
print('students: {}'.format(students))




students = ['홍길동', '박찬호', '이용규', '강호동']
print(students)
print(type(students))


students = ('홍길동', '박찬호', '이용규', '강호동')
print(students)
print(type(students))


students = '홍길동', '박찬호', '이용규', '강호동'
print(students)
print(type(students))




students = ['홍길동', '박찬호', '이용규', '강호동']
print(students)
print(type(students))

students = tuple(students)
print(students)
print(type(students))



students = list(students)
print(students)
print(type(students))






playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print('playerScore: {}'.format(playerScore))
print(type(playerScore))

playerScore = list(playerScore)
print(type(playerScore))

playerScore.sort()
print('playerScore: {}'.format(playerScore))
playerScore.pop(0)
playerScore.pop(len(playerScore) - 1)

playerScore = tuple(playerScore)
print('playerScore: {}'.format(playerScore))
print(type(playerScore))

sum = 0
avg = 0
for score in playerScore:
    sum += score

avg = sum / len(playerScore)

print('총점: %.2f' % sum)
print('평점: %.2f' % avg)