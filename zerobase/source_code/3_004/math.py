inputNumber = int(input('1보다 큰 정수 입력: '))

n = 2
while n <= inputNumber:
    if inputNumber % n == 0:
        print('소인수: {}'.format(n))
        inputNumber /= n
    else:
        n += 1





inputNumber = int(input('1보다 큰 정수 입력: '))

n = 2
searchNumbers = []
while n <= inputNumber:
    if inputNumber % n == 0:
        print('소인수: {}'.format(n))
        if searchNumbers.count(n) == 0:
            searchNumbers.append(n)
        elif searchNumbers.count(n) == 1:
            searchNumbers.remove(n)
        inputNumber /= n
    else:
        n += 1

print('searchNumbers: {}'.format(searchNumbers))

resultNumber = 1
for num in searchNumbers:
    resultNumber *= num

print('어떤 수의 제곱을 만들 수 있는 가장 작은 정수: {}'.format(resultNumber))

