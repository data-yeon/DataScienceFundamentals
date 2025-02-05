import nearMod

uWeight = float(input('input weight(Kg): '))
uHeight = float(input('input height(m): '))

na = nearMod.BmiAlgorithm(uWeight, uHeight)
na.calculatorBMI()
na.printUserCondition()

