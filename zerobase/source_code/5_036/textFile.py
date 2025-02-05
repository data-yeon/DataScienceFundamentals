uri = 'C:/pythonTxt/'

# 'w' 파일 모드
file = open(uri + 'hello.txt', 'w')

strCnt = file.write('Hello world!!')
print(f'strCnt: {strCnt}')

file.close()


file = open(uri + 'hello.txt', 'w')

strCnt = file.write('Hello Python!!')
print(f'strCnt: {strCnt}')

file.close()


# 'a' 파일 모드
file = open(uri + 'hello.txt', 'a')

file.write('\n')
file.write('Hello data science!!')

file.close()


# 'x' 파일 모드
file = open(uri + 'hello.txt', 'x')

file.write('Nice to meet you!!')

file.close()


# 'r' 파일 모드
file = open(uri + 'hello.txt', 'r')

str = file.read()
print(f'str: {str}')

file.close()


uri = 'C:/pythonTxt/'

def writePrimeNumber(n):
    file = open(uri + 'prime_numbers.txt', 'a')
    file.write(str(n))
    file.write('\n')

    file.close()

inputNumber = int(input("0보다 큰 정수 입력: "))
for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break

    if (flag):
        writePrimeNumber(number)
