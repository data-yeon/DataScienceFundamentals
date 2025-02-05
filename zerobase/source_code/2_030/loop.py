from builtins import range

for i in range(5):
    print('Hello~')

for j in range(10):
    result = 7 * j
    print('{} * {} = {}'.format(7, j, result))

for k in range(10):
    pass

for h in range(5):
    print('Hi!', end= '')
    print(' loop statement!')


for num in range(5):
    print('Hello python!')


gugudanNum = int(input('희망 구구단 입력 : '))

for num in range(9):
    result = gugudanNum * (num + 1)
    print('{} * {} = {}'.format(gugudanNum, (num + 1), result))