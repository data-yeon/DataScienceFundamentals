money50000 = 50000; money10000 = 10000; money5000 = 5000; money1000 = 1000;
money500 = 500; money100 = 100; money10 = 10

money50000Cnt = 0; money10000Cnt = 0; money5000Cnt = 0; money1000Cnt = 0;
money500Cnt = 0; money100Cnt = 0; money10Cnt = 0

productPrice = int(input('상품 가격 입력: '))
payPrice = int(input('지불 금액: '))


if payPrice > productPrice:
    changeMoney = payPrice - productPrice
    changeMoney = (changeMoney // 10) * 10
    print('거스름 돈: {}(원단위 절사)'.format(changeMoney))

if changeMoney > money50000:
    money50000Cnt = changeMoney // money50000
    changeMoney %= money50000

if changeMoney > money10000:
    money10000Cnt = changeMoney // money10000
    changeMoney %= money10000

if changeMoney > money5000:
    money5000Cnt += changeMoney // money5000
    changeMoney %= money5000

if changeMoney > money1000:
    money1000Cnt += changeMoney // money1000
    changeMoney %= money1000

if changeMoney > money500:
    money500Cnt += changeMoney // money500
    changeMoney %= money500

if changeMoney > money100:
    money100Cnt += changeMoney // money100
    changeMoney %= money100

if changeMoney > money10:
    money10Cnt += changeMoney // money10
    changeMoney %= money10

print('-' * 30)
print('50,000 {}장'.format(money50000Cnt))
print('10,000 {}장'.format(money10000Cnt))
print('5,000 {}장'.format(money5000Cnt))
print('1,000 {}장'.format(money1000Cnt))
print('500 {}개'.format(money500Cnt))
print('100 {}개'.format(money100Cnt))
print('10 {}개'.format(money10Cnt))
print('-' * 30)