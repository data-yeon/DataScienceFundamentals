num = 0
while True:
    print('Hello~ ')

    num += 1
    if (num >= 5):
        break




sum = 0
searchNum = 0
for i in range(100):
    sum += i

    if sum > 100:
        searchNum = i
        break

print('searchNum: {}'.format(searchNum))




result = 1
num = 0
for i in range(1, 11):
    result *= i

    if result > 50:
        num = i
        break

print('num: {}, result: {}'.format(num, result))




limitWeight = 2200
currentWeight = 800
date = 1

while True:
    if currentWeight >= 2200:
        break

    date += 1
    currentWeight += 70

print('이유식 중단 날짜: {}일'.format(date))

