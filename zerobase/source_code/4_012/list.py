students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '강호동']
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))

rValue= students.pop()
print('return value: {}'.format(rValue))
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))


students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))

rValue= students.pop(3)
print('return value: {}'.format(rValue))
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))



playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print('playerScore : {}'.format(playerScore))

minScore = 0; maxScore = 0
minScoreIdx = 0; maxScoreIdx = 0

for idx, score in enumerate(playerScore):
    if idx == 0 or minScore > score:
        minScoreIdx = idx
        minScore = score

print('minScore:{}, minScoreIdx : {}'.format(minScore, minScoreIdx))

playerScore.pop(minScoreIdx)
print('playerScore : {}'.format(playerScore))

for idx, score in enumerate(playerScore):
    if maxScore < score:
        maxScoreIdx = idx
        maxScore = score

print('maxScore:{}, maxScoreIdx : {}'.format(maxScore, maxScoreIdx))

playerScore.pop(maxScoreIdx)
print('playerScore : {}'.format(playerScore))







