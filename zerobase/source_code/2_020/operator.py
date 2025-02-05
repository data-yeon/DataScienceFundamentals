print('{} and {} : {}'.format(True, True, (True and True)))
print('{} and {} : {}'.format(False, True, (False and True)))
print('{} and {} : {}'.format(True, False, (True and False)))
print('{} and {} : {}'.format(False, False, (False and False)))


print('{} or {} : {}'.format(True, True, (True or True)))
print('{} or {} : {}'.format(False, True, (False or True)))
print('{} or {} : {}'.format(True, False, (True or False)))
print('{} or {} : {}'.format(False, False, (False or False)))


print('not {} : {}'.format(True, (not True)))
print('not {} : {}'.format(False, (not False)))

# age = int(input('나이 입력 : '))
# vaccine = (age < 20) or (age >= 65)
# print('age: {}, result: {}'.format(age, vaccine))


passScore1 = 60
passScore2 = 70

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

scoreAvg = (korScore + engScore + matScore) / 3
scoreAvgResult = scoreAvg >= passScore2

korResult = korScore >= passScore1
engResult = engScore >= passScore1
matResult = matScore >= passScore1

subjectResult = korResult and engResult and matResult

print('평균: {}, 결과: {}'.format(scoreAvg, scoreAvgResult))

print('국어: {}, 결과: {}'.format(korScore, korResult))
print('영어: {}, 결과: {}'.format(engScore, engResult))
print('수학: {}, 결과: {}'.format(matScore, matResult))
print('과락 결과: {}'.format(subjectResult))

print('최종 결과: {}'.format(scoreAvgResult and subjectResult))