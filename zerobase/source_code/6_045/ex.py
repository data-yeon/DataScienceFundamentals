import mod

num1 = int(input(f'input number1: '))
num2 = int(input(f'input number2: '))
ns = mod.NumsSum(num1, num2)
result = ns.sumBetweenNums()
print(f'result: {result}')

