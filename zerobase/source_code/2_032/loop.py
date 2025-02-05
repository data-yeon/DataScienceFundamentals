endNum = 10
n = 0

while n <= endNum:
    print(n)
    n += 1

n = 1
while n < 10:
    result = 7 * n
    print('{} * {} = {}'.format(7, n, result))
    n += 1

while n > 10:
    pass

n = 1
while n < 10:
    print('Hi', end='')
    print(' loop statement!')
    n += 1

n = 1
while n < 101:
    if n % 2 == 0:
        print('{}은 2의 배수이다.'.format(n))

    if n % 3 == 0:
        print('{}은 3의 배수이다.'.format(n))

    n += 1

gugudanNum = int(input('희망 구구단 입력 : '))

n = 1
while n < 10:
    result = gugudanNum * n
    print('{} * {} = {}'.format(gugudanNum, n, result))
    n += 1