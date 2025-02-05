productPrice = int(input("상품 가격 입력: "))
payPrice = int(input('지불 금액: '))

if payPrice > productPrice:
    changeMoney = payPrice - productPrice
    print(changeMoney)
    changeMoneyStr = changeMoney //10
    print(changeMoney)