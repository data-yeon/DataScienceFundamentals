cars = ('그랜저', '소나타', '말리부', '카니발', '쏘렌토')

n = 0
while n < len(cars):
    print(cars[n])
    n += 1


n = 0
flag = True
while flag:
    print(cars[n])
    n += 1

    if n == len(cars):
        flag = False


n = 0
while True:
    print(cars[n])
    n += 1

    if n == len(cars):
        break


studentCnts = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

n = 0
while n < len(studentCnts):
    print('{}학급 학생수: {} '.format(studentCnts[n][0], studentCnts[n][1]))
    n += 1


# 학급 학생수
studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
sum = 0
avg = 0
n = 0
while n < len(studentCnts):
    classNo = studentCnts[n][0]
    cnt = studentCnts[n][1]
    print('{}학급 학생수: {}명'.format(classNo, cnt))

    sum += cnt
    n += 1

print('전체 학생 수: {}명'.format(sum))
print('평균 학생 수: {}명'.format(sum / len(studentCnts)))