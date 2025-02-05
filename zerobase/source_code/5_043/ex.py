def formatedNumber(n):
    return format(n, ',')


def recursionFun(n):

    if n == 1:
        return n
    return n * recursionFun(n - 1)

inputNumber = int(input('input number: '))
inputNumberFormated = formatedNumber(recursionFun(inputNumber))
print(inputNumberFormated)


# 단리 계산기
def singleRateCalculator(m, t, r):
    totalMoney = 0
    totalRateMoney = 0

    for i in range(t):
        totalRateMoney += m * (r * 0.01)

    totalMoney = m + totalRateMoney
    return int(totalMoney)


# 월복리 계산기
def multiRateCalculator(m, t, r):

    t = t * 12
    rpm = (r / 12) * 0.01
    totalMoney = m

    for i in range(t):
        totalMoney += totalMoney * rpm

    return int(totalMoney)



money = int(input('예치금(원): '))
term = int(input('기간(년): '))
rate = int(input('연 이율(%): '))

print()
print('[단리 계산기]')
print('=' * 30)
print(f'예치금\t: {formatedNumber(money)}원')
print(f'예치기간\t: {term}년')
print(f'연 이율\t: {rate}%')
print('-' * 30)
amount = formatedNumber(singleRateCalculator(money, term, rate))
print(f'{term}년 후 총 수령액: {amount}원')
print('=' * 30)


print()
print('[월복리 계산기]')
print('=' * 30)
print(f'예치금\t: {formatedNumber(money)}원')
print(f'예치기간\t: {term}년')
print(f'연 이율\t: {rate}%')
print('-' * 30)
amount = formatedNumber(multiRateCalculator(money, term, rate))
print(f'{term}년 후 총 수령액: {amount}원')
print('=' * 30)
