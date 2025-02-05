fruits = ({'수박':8}, {'포도':13}, {'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
fruits = list(fruits)

cIdx = 0; nIdx = 1
eIdx = len(fruits) - 1

flag = True
while flag:
    curDic = fruits[cIdx]
    nextDic = fruits[nIdx]

    curDicCnt = list(curDic.values())[0]
    nextDicCnt = list(nextDic.values())[0]

    if nextDicCnt < curDicCnt:
        fruits.insert(cIdx, fruits.pop(nIdx))
        nIdx = cIdx + 1
        continue

    nIdx += 1
    if nIdx > eIdx:
        cIdx += 1
        nIdx = cIdx + 1

        if cIdx == 5:
            flag = False

print(tuple(fruits))