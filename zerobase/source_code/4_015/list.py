students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students: {}'.format(students))

students.sort()
print('students: {}'.format(students))

students.sort(reverse=True)
print('students: {}'.format(students))


numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print('numbers: {}'.format(numbers))

numbers.sort()
print('students: {}'.format(numbers))

numbers.sort(reverse=True)
print('students: {}'.format(numbers))


playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print('playerScore: {}'.format(playerScore))

playerScore.sort()
print('playerScore: {}'.format(playerScore))
playerScore.pop(0)
playerScore.pop(len(playerScore) - 1)
print('playerScore: {}'.format(playerScore))

sum = 0
avg = 0
for score in playerScore:
    sum += score

avg = sum / len(playerScore)

print('총점: %.2f' % sum)
print('평점: %.2f' % avg)



