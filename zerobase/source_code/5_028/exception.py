def add(n1, n2):
    print(n1 + n2)

def sub(n1, n2):
    print(n1 - n2)

def mul(n1, n2):
    print(n1 * n2)

def div(n1, n2):
    print(n1 / n2)


firstNum = int(input('first number: '))
secondNum = int(input('second number: '))

add(firstNum, secondNum)
sub(firstNum, secondNum)
mul(firstNum, secondNum)
div(firstNum, secondNum)



# ZeroDivisionError: division by zero
print(10 / 0)

# ValueError: invalid literal for int() with base 10: 'Hello'
int('Hello')

# IndexError: list index out of range
tempList = [1, 2, 3, 4, 5]
print(tempList[0])
print(tempList[1])
print(tempList[2])
print(tempList[3])
print(tempList[4])
print(tempList[5])

# IndentationError: unexpected indent
# if 10 <= 20:
#     print('result: ', end='')
        # print('10 <= 20')

# FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/test.txt'
file = open('c:/python/test.txt', 'r')


# 예외 처리
try:
    print(10 / 0)
except:
    print('예외 발생!! 예외 확인 하세요.')