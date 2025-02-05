def calculator(n1, n2):
    result = n1 + n2

    return result


returnValue = calculator(20, 10)
print(f'returnValue: {returnValue}')



def divideNumber(n):

    if n % 2 == 0:
        result = '짝수'
    else:
        result = '홀수'

    return result

    # if n % 2 == 0:
    #     return '짝수'
    # else:
    #     return '홀수'

returnValue = divideNumber(5)
print(f'returnValue: {returnValue}')




def cmToMm(cm):
    result = cm * 10

    return result

length = float(input('길이(cm)입력: '))
returnValue = cmToMm(length)
print(f'returnValue: {returnValue}mm')




import random

def getOddRandomNumber():

    while True:
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break

    return rNum

print(f'returnValue: {getOddRandomNumber()}')


