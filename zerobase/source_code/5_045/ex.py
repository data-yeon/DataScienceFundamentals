def sequenceCal(n1, r, n):

    valueN = 0
    sumN = 0
    i = 1

    while i <= inputN:

        if i == 1:
            valueN = n1
            sumN += valueN
            print('{}번째 항의 값: {}'.format(i, valueN))
            print('{}번째 항까지의 합: {}'.format(i, sumN))
            i += 1
            continue

        valueN *= r
        sumN += valueN
        print('{}번째 항의 값: {}'.format(i, valueN))
        print('{}번째 항까지의 합: {}'.format(i, sumN))
        i += 1



def sequenceCal01(n1, r, n):

    # 등비 수열(일반항) 공식: an = a1 * r^(n-1)
    valueN = n1 * (r ** (n - 1))
    print('{}번째 항의 값: {}'.format(n, valueN))

    # 등비 수열(합) 공식: sn = a1 * (1 - r^n) / (1-r)
    sumN = n1 * (1 - (r ** n)) / (1 - r)
    print('{}번째 항까지의 합: {}'.format(n, int(sumN)))



inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))


sequenceCal(inputN1, inputR, inputN)
print('-' * 50)
sequenceCal01(inputN1, inputR, inputN)


