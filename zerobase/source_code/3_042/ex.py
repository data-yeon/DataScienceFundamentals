# 9P4, 6P2
numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))
result = 1

for n in range(numN, (numN-numR), -1):
    print('n : {}'.format(n))
    result *= n

print('result: {}'.format(result))





fNum1 = int(input('factorial1: '))
result1 = 1

for n in range(fNum1, 0, -1):
    result1 *= n
print('result1: {}'.format(result1))


fNum2 = int(input('factorial2: '))
result2 = 1

for n in range(fNum2, 0, -1):
    result2 *= n
print('result2: {}'.format(result2))

print('모든 경우의 수: {}'.format(result1 * result2))






import math

result1 = math.factorial(fNum1)
result2 = math.factorial(fNum2)
print('모든 경우의 수: {}'.format(result1 * result2))