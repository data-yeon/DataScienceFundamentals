inputN = int(input('n항 입력: '))

flag = True
n = 1; nCnt = 1; searchN = 0
while flag:

    for i in range(1, (n + 1)):
        if i == n:
            print('{} '.format(i), end='')
        else:
            print('{}, '.format(i), end='')

        nCnt += 1
        if (nCnt > inputN):
            searchN = i
            flag = False
            break

    print()
    n += 1

print('{}항: {}'.format(inputN, searchN))




inputN = int(input('n항 입력: '))

flag = True
n = 1; nCnt = 1; searchNC = 0; searchNP = 0
while flag:

    for i in range(1, (n + 1)):
        if i == n:
            print('{}/{} '.format(i, (n - i + 1)), end='')
        else:
            print('{}/{}, '.format(i, (n - i + 1)), end='')

        nCnt += 1
        if (nCnt > inputN):
            searchNC = i
            searchNP = n - i + 1
            flag = False
            break

    print()
    n += 1

print('{}항: {}/{}'.format(inputN, searchNC, searchNP))