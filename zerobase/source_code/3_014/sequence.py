inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
sumN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        sumN += valueN
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valueN += inputD
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, sumN))


# 등차 수열(합) 공식: sn = n(a1 + an) / 2
valueN = inputN1 + (inputN-1) * inputD
sumN = inputN * (inputN1 + valueN) / 2
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))

