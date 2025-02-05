minAblePoint = 1000

userPoint = int(input('고객 포인트 입력 : '))

print('포인트 사용 가능') if userPoint >= minAblePoint else print('포인트 사용 불가능')

result = '가능' if userPoint >= minAblePoint else '불가능'
print('포인트 사용 가능 여부 : {}'.format(result))


if userPoint >= minAblePoint:
    print('포인트 사용 가능')
else:
    print('포인트 사용 불가능')


if userPoint >= minAblePoint:
    result = '가능'
else:
    result = '불가능'

print('포인트 사용 가능 여부 : {}'.format(result))


if userPoint >= minAblePoint:
    result = '가능'
else:
    result = '불가능'
    lackPoint = minAblePoint - userPoint
    print('포인트가 {}부족합니다.'.format(lackPoint))

print('포인트 사용 가능 여부 : {}'.format(result))

rainPercentage = int(input('비올 확률 입력 : '))
minRainPercentage = 55

print('우산을 챙기세요.') if rainPercentage >= minRainPercentage else print('양산을 챙기세요.')

if rainPercentage >= minRainPercentage:
    print('우산을 챙기세요.')
else:
    print('양산을 챙기세요.')
    

limTemp = 11
lowTemp = int(input('최저 기온 입력 : '))
higTemp = int(input('최고 기온 입력 : '))
gapTemp = higTemp - lowTemp

if gapTemp >= 11:
    print('일교차 : {}'.format(gapTemp))
    print('감기 조심하세요.')
else:
    print('일교차 : {}'.format(gapTemp))
    print('산책하기 좋은 날씨입니다.')
