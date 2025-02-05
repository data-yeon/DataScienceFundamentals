def getPermutaionCnt(n, r, logPrint = True):

    result = 1
    for n in range(n, (n-r), -1):
        if logPrint: print('n : {}'.format(n))
        result = result * n

    return result



from itertools import permutations

def getPermutaions(ns, r):

    pList = list(permutations(ns, r))
    print(f'{len(ns)}P{r} 개수: {len(pList)}')

    for n in permutations(ns, r):
        print(n, end=', ')



if __name__ == '__main__':
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))


    print(f'{numN}P{numR}: {getPermutaionCnt(numN, numR, logPrint=False)}')

    ns = [1, 2, 3, 4, 5, 6, 7, 8]
    getPermutaions(ns, 3)


