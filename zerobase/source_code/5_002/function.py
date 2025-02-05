def addCal():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))
    print(f'n1 + n2 = {n1 + n2}')


addCal()



def printWeatherInfo():
    print('오늘 날씨는 맑습니다. 기온은 25도입니다.')

printWeatherInfo()
printWeatherInfo()
printWeatherInfo()



def calFun():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))

    print(f'n1 * n2 = {n1 * n2}')
    print(f'n1 / n2 = {round(n1 / n2, 2)}')

calFun()