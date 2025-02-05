for i in range(100):
    if i % 7 != 0:
        continue

    print('{}는 7의 배수입니다.'.format(i))

cnt = 0
for i in range(100):
    if i % 7 != 0:
        continue

    print('{}는 7의 배수입니다.'.format(i))
    cnt += 1

else:
    print('99까지의 정수 중 7의 배수는 {}개입니다.'.format(cnt))


minNum = 0
for i in range(1, 101):
    if i % 3 != 0 or i % 7 != 0:
        continue

    print('공배수: {}'.format(i))

    if minNum == 0:
        minNum = i

else:
    print('최소 공배수: {}'.format(minNum))

