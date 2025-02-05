def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return total / len(ns)

def getMax(ns):

    maxN = ns[0]
    for n in ns:
        if maxN < n:
            maxN = n

    return maxN

def getDeviation(n1, n2):
    return round(abs(n1 - n2), 2)