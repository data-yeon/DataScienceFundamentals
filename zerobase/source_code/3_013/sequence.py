inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue

    valueN += inputD
    print('{}번째 항의 값: {}'.format(n, valueN))
    n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))


# 등차 수열(일반항) 공식: an = a1 + (n-1) * d
valueN = inputN1 + (inputN-1) * inputD
print('{}번째 항의 값: {}'.format(inputN, valueN))




