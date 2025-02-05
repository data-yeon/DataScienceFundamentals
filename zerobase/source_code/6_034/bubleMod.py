import copy

def sortBybubleSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    length = len(c_ns) - 1
    for i in range(length):
        for j in range(length-i):

            if asc:
                if c_ns[j] > c_ns[j+1]:
                    c_ns[j], c_ns[j+1] = c_ns[j+1], c_ns[j]
            else:
                if c_ns[j] < c_ns[j+1]:
                    c_ns[j], c_ns[j+1] = c_ns[j+1], c_ns[j]

            print(f'ns: {c_ns}')
        print()

    return c_ns

