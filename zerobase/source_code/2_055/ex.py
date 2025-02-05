import random

rNum = random.randint(1, 1000)
tryCount = 0;
gameFlag = True

while gameFlag:
    tryCount += 1
    pNum = int(input('1에서 1000까지의 정수 입력: '))

    if rNum == pNum:
        print('빙고!')
        gameFlag = False
    else:
        if rNum > pNum:
            print('난수가 크다!')
        else:
            print('난수가 작다!')

print('난수: {}, 시도 횟수: {}'.format(rNum, tryCount))



innerTemp = float(input('실내온도 입력: '))

if innerTemp <= 18:
    print('에어컨: OFF!!')
elif innerTemp > 18 and innerTemp <= 22:
    print('에어컨: 매우 약!!')
elif innerTemp > 22 and innerTemp <= 24:
    print('에어컨: 약!!')
elif innerTemp > 24 and innerTemp <= 26:
    print('에어컨: 중!!')
elif innerTemp > 26 and innerTemp <= 28:
    print('에어컨: 강!!')
elif innerTemp > 28:
    print('에어컨: 매우 강!!')



