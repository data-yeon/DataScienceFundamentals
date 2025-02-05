hou = int(input('시간 입력: '))
min = int(input('분 입력: '))
sec = int(input('초 입력: '))

print('{}초'.format(format(hou * 60 * 60 + min * 60 + sec, ',')))




money = int(input('금액 입력: '))
rate = float(input('이율 입력: '))
term = int(input('기간 입력: '))

targetMoney = money

for i in range(term):
    targetMoney += (targetMoney * rate * 0.01)

targetMoneyFormated = format(int(targetMoney), ',')

print('-' * 30)
print('이율: {}%'.format(rate))
print('원금: {}원'.format(format(money, ',')))
print('{}년 후 금액: {}원'.format(term, targetMoneyFormated))
print('-' * 30)

