def searchNumberByLineAlgorithm(ns, sn):

    searchResultIdx = -1

    print(f'Numbers: {ns}')
    print(f'Search Numbers: {sn}')

    n = 0
    while True:

        if n == len(ns):
            print('Search FAIL!!')
            break

        if ns[n] == sn:
            searchResultIdx = n
            print('Search SUCCESS!!')
            print(f'Search result INDEX: {searchResultIdx}')
            break

        n += 1

    return searchResultIdx