ship1 = 3; ship2 = 4; ship3 = 5
maxDay = 0

for i in range(1, (ship1 + 1)):
    if ship1 % i == 0 and ship2 % i == 0:
        maxDay = i

# print('최대공약수: {}'.format(maxDay))

minDay = (ship1 * ship2) // maxDay
# print('{}, {}의 최소공배수: {}'.format(ship1, ship2, minDay))


newDay = minDay
for i in range(1, (newDay + 1)):
    if newDay % i == 0 and ship3 % i == 0:
        maxDay = i

# print('최대공약수: {}'.format(maxDay))

minDay = (newDay * ship3) // maxDay
# print('{}, {}, {}의 최소공배수: {}'.format(ship1, ship2, ship3, minDay))

# print('{}일마다 모든 선박이 입항합니다.'.format(minDay))


from datetime import datetime
from datetime import timedelta

n = 1
baseTime = datetime(2021, 1, 1, 10, 0, 0)
# baseTime = datetime.now()

# print(f'2021년 모든 선박 입항일: {baseTime}')
with open('C:/pythonTxt/arrive.txt', 'a') as f:
    f.write(f'2021년 모든 선박 입항일\n')
    f.write(f'{baseTime}\n')

nextTime = baseTime + timedelta(days=minDay)
while True:

    # print(f'2021년 모든 선박 입항일: {nextTime}')
    with open('C:/pythonTxt/arrive.txt', 'a') as f:
        f.write(f'{nextTime}\n')

    nextTime = nextTime + timedelta(days=minDay)
    if nextTime.year > 2021:
        break


