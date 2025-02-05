def greet():
    print('안녕하세요.')

greet()

def greet(customer):
    print(f'{customer} 고객님 안녕하세요.')

greet('홍길동')


def calculator(n1, n2):
    print(f'{n1} + {n2} = {n1+n2}')
    print(f'{n1} - {n2} = {n1-n2}')
    print(f'{n1} * {n2} = {n1*n2}')
    print(f'{n1} / {n2} = {n1/n2}')

calculator(20, 10)



def addFun(n1, n2):
    print(f'{n1} + {n2} = {n1+n2}')

addFun(10, 20)



def printNumber(*numbers):
    for number in numbers:
        print(number, end='')
    print()

printNumber()
printNumber(1)
printNumber(1, 2)
printNumber(1, 2, 3)
printNumber(1, 2, 3, 4)
printNumber(1, 2, 3, 4, 5)




def printScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3

    print(f'총점: {sum}')
    print(f'평균: {round(avg, 2)}')

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

printScore(korScore, engScore, matScore)



def printScore(*scores):
    sum = 0
    for score in scores:
        sum += score
    avg = sum / len(scores)

    print(f'총점: {sum}')
    print(f'평균: {round(avg, 2)}')

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))
sciScore = int(input('과학 점수 입력: '))
hisScore = int(input('국사 점수 입력: '))

printScore(korScore, engScore, matScore, sciScore, hisScore)
