import datetime

today = datetime.datetime.today()
day = today.day

limitDust = 150
dustNum = int(input('미세먼지 수치 입력: '))
carType = int(input('차량 종류 선택. 1.승용차 \t 2.영업용차 '))
carNumer = int(input('차량 번호 입력: '))

print('-' * 30)
print(today)
print('-' * 30)
if dustNum > limitDust and carType == 1:
    if (day % 2) == (carNumber % 2):
        print('차량 2부제 적용')
        print('차량 2부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dustNum > limitDust and carType == 2:
    if (day % 5) == (carNumber % 5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')
if dustNum <= limitDust:
    if (day % 5) == (carNumber % 5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')
print('-' * 30)