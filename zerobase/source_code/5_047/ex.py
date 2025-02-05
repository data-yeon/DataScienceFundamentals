import  discount as dc

if __name__ == '__main__':
    flag = True
    gs = []

    while flag:
        selectNumber = int(input('상품을 구매 하시겠어요? 1.구매 2.종료 '))

        if selectNumber == 1:
            goods_price = int(input('상품 가격 입력: '))
            gs.append(goods_price)

        elif selectNumber == 2:
            result = dc.calculatorTotalPrice(gs)
            flag = False


    print(f'할인율: {result[0]}')
    print(f'합계: {dc.formatedNumber(result[1])}원')