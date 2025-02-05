#1부터 10까지의 합을 구한다.
sum = 0
for i in range(1, 11):
    sum += i
print('sum : {}'.format(sum))

sum = 0
n = 1
while n < 11:
    sum += n
    n += 1
print('sum : {}'.format(sum))

# 1부터 시작해서 7의 배수의 합이 50이상인 최초의 정수 출력
sum = 0
maxInt = 0
for i in range(1, 101):

    if i % 7 == 0 and sum <= 50:
        sum += i
        maxInt = i

    print('i : {}'.format(i))

print('7의 배수의 합이 50이상인 최초의 정수 : {}'.format(maxInt))

# 1부터 시작해서 7의 배수의 합이 50이상인 최초의 정수 출력
sum = 0
maxInt = 0
n = 1
while n <= 100 and sum <= 50:
    n += 1

    if n % 7 == 0:
        sum += n
        maxInt = n

    print('n : {}'.format(n))

print('7의 배수의 합이 50이상인 최초의 정수 : {}'.format(maxInt))

currentThickness = 30
rotationCount = 0
removeThickness = 0.15

while currentThickness >= 20:
    rotationCount += 1
    currentThickness -= removeThickness

safeRotationCount = rotationCount - 1
print('운행 가능 횟수 : {}'.format(safeRotationCount))