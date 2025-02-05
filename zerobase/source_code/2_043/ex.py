BMI = 몸무게(kg) / 신장(m) * 신장(m)

weight = input('체중 입력(g): ')
height = input('신장 입력(cm): ')

if weight.isdigit():
    weight = int(weight) / 10

if height.isdigit():
    height = int(height) / 100

print('체중: {}kg'.format(weight))
print('신장: {}m'.format(height))

bmi = weight / (height * height)
print('BMI : %.2f' % bmi)





num1 = 10
num2 = 20
print('num1: {}, num2: {}'.format(num1, num2))

tempNum = num1
num1 = num2
num2 = tempNum
print('num1: {}, num2: {}'.format(num1, num2))


score1 = input('중간 고사 점수: ')
score2 = input('기말 고사 점수: ')

if score1.isdigit() and score2.isdigit():
    score1 = int(score1)
    score2 = int(score2)

    totalScore = score1 + score2
    avgScore = totalScore / 2

    print('총점: {}, 평균: {}'.format(totalScore, avgScore))
else:
    print('잘 못 입력했습니다.')


