for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()



for i1 in range(1, 6):
    for i2 in range(6 - i1 - 1):
        print(' ', end='')

    for i3 in range(i1):
        print('*', end='')

    print()



for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()



for i in range(5, 0, -1):
    for j in range(5 - i):
        print(' ', end='')

    for j in range(i):
        print('*', end='')
    print()



for i in range(1, 10):
    if i < 5:
        for j in range(i):
            print('*', end='')
    else:
        for j in range(10-i):
            print('*', end='')
    print()



for i in range(1, 6):
    for j in range(1, 6):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()



for i in range(5, 0, -1):
    for j in range(1, 6):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()



for i1 in range(1, 6):
    for i2 in range(5 - i1):
        print(' ', end='')

    for n3 in range(i1 * 2 - 1):
        print('*', end='')

    print()



for i1 in range(1, 6):
    for i2 in range(i1 - 1):
        print(' ', end='')

    for n3 in range(11 - (i1 * 2)):
        print('*', end='')

    print()