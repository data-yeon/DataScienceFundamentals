num1 = 20
fNum1 = 3.14
result = num1 * fNum1
print('result : {}'.format(result))
print('result : %.2f' % result)

str1 = 'Hi '
result = str1 * 7
print('result : {}'.format(result))

num1 = 10
num2 = 3
result = num1 / num2
print('num1 : {}, num2 : {}'.format(num1, num2))
print('result : {}'.format(result))
print('result : %.2f' % result)

num1 = 0
num2 = 3
result = num1 / num2
print('result : {}'.format(result))


num1 = 0
num2 = 3
result = num2 / num1
print('result : {}'.format(result))


num1 = 20
num2 = 10
result = num1 / num2
print('result : {}'.format(result))
print('type of result : {}'.format(type(result)))

result = int(num1 / num2)
print('result : {}'.format(result))
print('type of result : {}'.format(type(result)))


kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

total = kor + eng + mat
print('국어 점수 {}'.format(kor))
print('영어 점수 {}'.format(eng))
print('수학 점수 {}'.format(mat))
print('합계 {}'.format(total))
print('평균 {}'.format(total / 3))
print('평균 %.2f' % (total / 3))


allStuCnt = int(input('전체 학생 수 : '))
stuCntOfGroup = int(input('한 모둠 학생 수 : '))
groupCnt = allStuCnt / stuCntOfGroup

print('전체 학생 수 : {}'.format(allStuCnt))
print('한 모둠 학생 수 : {}'.format(stuCntOfGroup))
print('모둠 수 : {}'.format(groupCnt))
print('모둠 수 : {}'.format(int(groupCnt)))