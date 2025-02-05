def sequenceCal(n1, d, n):

    valueN = 0
    sumN = 0
    i = 1
    while i <= n:

        if i == 1:
            valueN = n1
            sumN += valueN
            print('{}번째 항의 값: {}'.format(i, valueN))
            print('{}번째 항까지의 합: {}'.format(i, sumN))
            i += 1
            continue

        valueN += d
        sumN += valueN
        print('{}번째 항의 값: {}'.format(i, valueN))
        print('{}번째 항까지의 합: {}'.format(i, sumN))
        i += 1


def sequenceCal01(n1, d, n):

    # 등차 수열(일반항) 공식: an = a1 + (n-1) * d
    valueN = n1 + (n-1) * d
    print('{}번째 항의 값: {}'.format(n, valueN))

    # 등차 수열(합) 공식: sn = n(a1 + an) / 2
    sumN = n * (n1 + valueN) / 2
    print('{}번째 항까지의 합: {}'.format(n, int(sumN)))


inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

sequenceCal(inputN1, inputD, inputN)
print('-' * 50)
sequenceCal01(inputN1, inputD, inputN)



