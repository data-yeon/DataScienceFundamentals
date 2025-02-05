'''
오전 6시 첫차 : 오후 23시 운행 종료
A버스 : 15분 간격 운행
B버스 : 13분 간격 운영

6시 20분 첫차 : 오후 22시 운행 종료
C버스 : 8분 간격 운행

집앞 버스 정류장에서 학교까지 가는 버스 A,B,C의 운행정보가 다음과 같을 때, 2대 이상의 버스가 정차하는 시간대를 출력해보자.
'''

busA = 15
busB = 13
busC = 8

totalMin = 17 * 60
for i in range(totalMin + 1):
    if i < 20 or i > (totalMin - 60):
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour, min))
    else:
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour, min))
        elif i % busA == 0 and i % busC == 0:
            print('busA와 busC 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour, min))
        elif i % busB == 0 and i % busC == 0:
            print('busB와 busC 동시 정차!!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{}:{}'.format(hour, min))




