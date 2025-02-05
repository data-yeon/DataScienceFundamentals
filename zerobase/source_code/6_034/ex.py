import random
import bubleMod

if __name__ == '__main__':
    nums = random.sample(range(1, 20), 10)
    print(f'not sorted nums: {nums}')

    result = bubleMod.sortBybubleSortAlgorithm(nums)
    print(f'sorted nums by ASC: {result}')

    result = bubleMod.sortBybubleSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC: {result}')