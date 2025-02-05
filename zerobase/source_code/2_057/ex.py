fNum = int(input('정수 입력: '))

addSum = 0
for i in range(1, (fNum+1)):
    addSum += i

addSumFormated = format(addSum, ',')
print('합 결과 : {}'.format(addSumFormated))



oddSum = 0
for i in range(1, (fNum+1)):
    if i % 2 != 0:
        oddSum += i

oddSumFormated = format(oddSum, ',')
print('홀수 합 결과 : {}'.format(oddSumFormated))



enenSum = 0
for i in range(1, (fNum+1)):
    if i % 2 == 0:
        enenSum += i

enenSumFormated = format(enenSum, ',')
print('짝수 합 결과 : {}'.format(enenSumFormated))



factorialResult = 1
for i in range(1, (fNum+1)):
    factorialResult *= i

factorialResultFormated = format(factorialResult, ',')
print('팩토리얼 결과 : {}'.format(factorialResultFormated))


