import lineMod
import random

if __name__ == '__main__':

    rNums = random.sample(range(1, 21), 10)
    searchNum = int(input('input search number: '))

    resultIdx = lineMod.searchNumberByLineAlgorithm(rNums, searchNum)
    if resultIdx == -1:
        print('No resutls found')
        print(f'search result index: {resultIdx}')

    else:
        print('>>> Search Results <<<')
        print(f'search result index: {resultIdx}')
        print(f'search result number: {rNums[resultIdx]}')
