sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

def salesUpAndDown(ss):

    if len(ss) == 1:
        return ss

    print(f'sales: {ss}')
    currentSales = ss.pop(0)
    nextSales = ss[0]
    increase = nextSales - currentSales
    if increase > 0:
        increase = '+' + str(increase)
    print(f'매출 증감액: {increase}')

    return salesUpAndDown(ss)

if __name__ == '__main__':
    salesUpAndDown(sales)