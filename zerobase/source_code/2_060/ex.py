'''
톱니가 각가 7개와 12개의 톱니바퀴가 서로 맞물려 회전할 때,
회전을 시작한 후 처음 맞물린 톱니가 최초로 다시 만나게 될때까지의 톱니의 수와 각각의 바퀴 회전수를 출력해보자.
'''

gearATCnt = int(input('GearA 톱니수 입력: '))
gearBTCnt = int(input('GearB 톱니수 입력: '))

# gearBTCnt가 gearATCnt보다 크다고 가정한다.

gearA = 0
gearB = 0
leastNum = 0
flag = True
while flag:
    if gearA != 0:
        if gearA != leastNum:
            gearA += gearATCnt
        else:
            flag = False
    else:
        gearA += gearATCnt

    if gearB != 0 and gearB % gearATCnt == 0:
        leastNum = gearB
    else:
        gearB += gearBTCnt

    print('gearA: {}, gearB: {}'.format(gearA, gearB))

print('최초 만나는 톱니수(최소공배수): {}톱니'.format(leastNum))
print('gearA 회전수: {}회전'.format(int(leastNum / gearATCnt)))
print('gearB 회전수: {}회전'.format(int(leastNum / gearBTCnt)))





