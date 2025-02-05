import random

n = 1
while n < 10:
    print('Hello~ ')
    n += 1

flag = True
num = 0
sum = 0
while flag:
    num += 1
    sum += num
    print('{}까지의 합은 {}입니다.'.format(num, sum))

    if sum >= 1000:
        flag = False

import random

sum = 0
date = 1
flag = True

while flag:
    patientCount = random.randint(50, 100)
    sum += patientCount
    date += 1
    print('날짜: {}, \t 오늘 환자수: {}, \t 누적 환자수: {}'.format(date, patientCount, sum))

    if sum >= 10000:
        flag = False

