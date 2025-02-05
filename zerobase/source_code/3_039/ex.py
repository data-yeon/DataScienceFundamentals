#{2, 5, 11, 20, 32, 47, 65, 86, 110, 137, 167, …}

# (3n^2 - 3n + 4)/2 = an
inputA1 = int(input('a1 입력: '))
inputN = int(input('an 입력: '))

valueAN = ((3 * inputN ** 2) - (3 * inputN) + 4) / 2
print('an의 {}번째 항의 값: {}'.format(inputN, int(valueAN)))