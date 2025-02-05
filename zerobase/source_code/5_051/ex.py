import utilityBill as ub

inputIncome = int(input('수입 입력: '))
ub.setIncome(inputIncome)

inputWaterPrice = int(input('수도요금 입력: '))
ub.setWaterPrice(inputWaterPrice)

inputElectricPrice = int(input('전기요금 입력: '))
ub.setElectricPrice(inputElectricPrice)

inputGasPrice = int(input('가스요금 입력: '))
ub.setGasPrice(inputGasPrice)

print(f'공과금: {ub.formatedNumber(ub.getUtilityBill())}원')
print(f'수입 대비 공과금 비율: {ub.getUtilityBillRate()}%')


