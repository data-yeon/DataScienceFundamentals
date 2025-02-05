def getCombinationCnt(n, r, logPrint = True):

    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(n, (n - r), -1):
        resultP = resultP * n
    if logPrint: print('resultP : {}'.format(resultP))


    for n in range(r, 0, -1):
        resultR = resultR * n
    if logPrint: print('resultR: {}'.format(resultR))

    resultC = int(resultP / resultR)
    if logPrint: print('resultC: {}'.format(resultC))

    return resultC



from itertools import combinations

def getCombinations(ns, r):

    cList = list(combinations(ns, r))
    print(f'{len(ns)}C{r} 개수: {len(cList)}')

    for n in combinations(ns, r):
        print(n, end=', ')



if __name__ == '__main__':
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))


    print(f'{numN}C{numR}: {getCombinationCnt(numN, numR, logPrint=False)}')

    ns = [1, 2, 3, 4, 5, 6, 7, 8]
    getCombinations(ns, 3)


