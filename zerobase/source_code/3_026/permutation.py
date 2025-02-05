# 8p3
numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))
result = 1

for n in range(numN, (numN-numR), -1):
    print('n : {}'.format(n))
    result = result * n

print('result: {}'.format(result))






resultC = 1
resultP = 1

for n in range(numN, 0, -1):
    resultC = resultC * n

for n in range((numN - numR), 0, -1):
    resultP = resultP * n

print('result: {}'.format(int(resultC/resultP)))




import math

result = int(math.factorial(numN) / math.factorial(numN - numR))
print('result: {}'.format(result))





n = int(input('친구 수 입력: '))
result = 1
for i in range(1, n):
    result *= i

print('result: {}'.format(result))


import math

result = int(math.factorial(n - 1))
print('result: {}'.format(result))