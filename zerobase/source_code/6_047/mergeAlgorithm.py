def mSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc=asc)
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

    mergedNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if asc:
            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergedNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergedNums.append(rightNums[rightIdx])
                rightIdx += 1

        else:
            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergedNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergedNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergedNums += leftNums[leftIdx:]
    mergedNums += rightNums[rightIdx:]

    print(f'mergedNums: {mergedNums}')
    return mergedNums