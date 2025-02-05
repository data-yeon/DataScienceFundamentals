message = input('메시지 입력: ')
lenMessage = len(message)
msgPrice = 50;

if lenMessage <= 50:
    msgPrice = 50
    print('SMS 발송!!')
else:
    msgPrice = 100
    print('MMS 발송!!')

print('메지지 길이: {}'.format(lenMessage))
print('메시지 발송 요금: {}원'.format(msgPrice))


carSpeed = int(input('속도 입력: '))
limitSpeed = 50

if carSpeed > 50:
    print('안전속도 위반!! 과태표 50,000원 부과 대상!!!')
else :
    print('안전속도 준수!!')



