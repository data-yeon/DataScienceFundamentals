inputN = int(input('n 입력: '))

result = 1
for n in range(1, inputN+1):
    result *= n

print('{} 팩토리얼: {}'.format(inputN, result))


result = 1
n = 1
while n <= inputN:
    result *= n
    n += 1

print('{} 팩토리얼: {}'.format(inputN, result))





def factorialFun(n):
    if n == 1: return 1

    return n * factorialFun(n - 1)

print('{} 팩토리얼: {}'.format(inputN, factorialFun(inputN)))





import math
math.factorial(inputN)

print('{} 팩토리얼: {}'.format(inputN, math.factorial(inputN)))