import unitConversion as uc

if __name__ == '__main__':
    inputNumber = int(input('길이(cm) 입력: '))

    returnValue = uc.cmToMm(inputNumber)
    print(f'{inputNumber}cm : {returnValue}mm')

    returnValue = uc.cmToInch(inputNumber)
    print(f'{inputNumber}cm : {returnValue}inch')

    returnValue = uc.cmToM(inputNumber)
    print(f'{inputNumber}cm : {returnValue}m')

    returnValue = uc.cmToFt(inputNumber)
    print(f'{inputNumber}cm : {returnValue}ft')


