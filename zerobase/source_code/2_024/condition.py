passScore = 80

myScore = int(input('점수 입력 : '))

if myScore >= passScore:
    print('PASS!!')

if myScore < passScore:
    print('FAIL!!')


if myScore >= passScore:
    print('PASS!!')
else:
    print('FAIL!!')


messageString = input('문자 메시지 입력 : ')

if len(messageString) >= 500:
    pass
else:
    pass


seniorAge = 65

passengerAge = int(input('나이 입력 : '))
if passengerAge >= seniorAge:
    print('무료 대상 승객입니다.')
else:
    print('유료 대상 승객입니다.')


floatNum = float(input('소수 입력 : '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum) + 1))
else:
    print('버림 : {}'.format(int(floatNum)))