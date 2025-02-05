# 수 두개의 공약수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))


# 수 두개의 최대공약수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수: {}'.format(i))
        maxNum = i

print('최대공약수: {}'.format(maxNum))




# 수 세개의 공약수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
num3 = int(input('1보다 큰 정수 입력: '))

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        print('공약수: {}'.format(i))



# 수 세개의 최대공약수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
num3 = int(input('1보다 큰 정수 입력: '))
maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        print('공약수: {}'.format(i))
        maxNum = i

print('최대공약수: {}'.format(maxNum))


# 유클리드 호제법
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

temp1 = num1; temp2 = num2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp

print('{}, {}의 최대공약수: {}'.format(num1, num2, temp1))

for n in range(1, (temp1 + 1)):
    if temp1 % n == 0:
        print('{}, {}의 공약수: {}'.format(num1, num2, n))


