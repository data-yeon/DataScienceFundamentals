def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return total / len(ns)

def getMin(ns):

    minN = ns[0]
    for n in ns:
        if minN > n:
            minN = n

    return minN

def getDeviation(n1, n2):
    return round(abs(n1 - n2), 2)

def getMaxOrMin(ns, maxFlag = True):

    resultN = ns[0]
    for n in ns:
        if maxFlag:
            if resultN < n:
                resultN = n
        else:
            if resultN > n:
                resultN = n

    return resultN