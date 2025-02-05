import permutation as pt

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

# print(f'{numN}P{numR}: {pt.getPermutaionCnt(numN, numR)}')
print(f'{numN}P{numR}: {pt.getPermutaionCnt(numN, numR, logPrint=False)}')



listVar = [1, 2, 3, 4, 5, 6, 7, 8]
rVar = 3
pt.getPermutaions(listVar, rVar)