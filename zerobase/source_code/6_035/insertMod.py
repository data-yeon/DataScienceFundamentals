import copy

def sortInsertSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    for i1 in range(1, len(c_ns)):
        i2 = i1 - 1
        cNum = c_ns[i1]

        if asc:     # ascending
            while c_ns[i2] > cNum and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        else:       # descending
            while c_ns[i2] < cNum and i2 >= 0:
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

        c_ns[i2+1] = cNum
        print(f'nums: {c_ns}')

    return c_ns