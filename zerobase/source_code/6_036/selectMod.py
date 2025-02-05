import copy

def sortSelectSortAlgorithm(ns, asc=True):

    c_ns = copy.copy(ns)

    for i in range(len(c_ns) - 1):
        minIdx = i

        for j in range(i + 1, len(c_ns)):

            if asc:     # ascending
                if c_ns[minIdx] > c_ns[j]:
                    minIdx = j
            else:       # descending
                if c_ns[minIdx] < c_ns[j]:
                    minIdx = j

        c_ns[i], c_ns[minIdx] = c_ns[minIdx], c_ns[i]

        print(f'nums: {c_ns}')

    return c_ns