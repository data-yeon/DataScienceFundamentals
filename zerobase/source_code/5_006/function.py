num_out = 10
def printNumbers():
    print(f'num_out: {num_out}')

printNumbers()
print(f'num_out: {num_out}')


num_out = 10
def printNumbers():
    num_out = 20
    print(f'num_out: {num_out}')

printNumbers()
print(f'num_out: {num_out}')


def printNumbers():
    num_in = 20
    print(f'num_in: {num_in}')

printNumbers()


def printNumbers():
    num_in = 20
    print(f'num_in: {num_in}')

print(f'num_in: {num_in}')



num_out = 10
def printNumbers():
    global num_out
    num_out = 20
    print(f'num_out: {num_out}')

printNumbers()
print(f'num_out: {num_out}')



def printArea():
    triangleArea = width * height / 2
    squareArea = width * height

    print(f'삼각형 넓이: {triangleArea}')
    print(f'사각형 넓이: {squareArea}')

width = int(input('가로 길이 입력: '))
height = int(input('세로 길이 입력: '))
printArea()



totalVisit = 0

def countTotalVisit():
    global totalVisit

    totalVisit = totalVisit + 1
    print(f'누적 방문객: {totalVisit}')

countTotalVisit()
countTotalVisit()
countTotalVisit()
countTotalVisit()
countTotalVisit()
