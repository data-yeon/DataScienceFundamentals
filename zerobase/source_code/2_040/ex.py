name = '홍길동'
product = '야구글러브'
orderNo = 2568956
payMethod = '신용카드'
productPrice = 110000
payPrice = 100000
usePoint = 10000
payDate = '2021/08/03 21:50:12'
payDiv = 6
payDivCategory = '무'
phone = '02-1234-5678'

print(name, '고객님 안녕하세요.')
print(name, '고객님의 주문이 완료되었습니다.')
print('다음은 주문건에 대한 상세 내역입니다.')
print('-------------------------------------')
print('상품명\t:', product)
print('주문번호\t:', orderNo)
print('결재방법\t:', payMethod)
print('상품금액\t:', productPrice, '원')
print('결재금액\t:', payPrice, '원')
print('포인트\t:', usePoint, 'P')
print('결제일시\t:', payDate)
print('할부\t\t:', payDiv, '개월')
print('할부유형\t:', payDivCategory)
print('문의\t:', phone)
print('-------------------------------------')
print('저희 사이트를 이용해 주셔서 감사합니다.')
