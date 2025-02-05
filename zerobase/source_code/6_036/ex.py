import random
import selectMod

if __name__ == '__main__':
    nums = random.sample(range(1, 20), 10)

    print(f'not sorted nums:\n{nums}')
    result = selectMod.sortSelectSortAlgorithm(nums)
    print(f'sorted nums by ASC:\n{result}')

    print(f'not sorted nums:\n{nums}')
    result = selectMod.sortSelectSortAlgorithm(nums, asc=False)
    print(f'sorted nums by DESC:\n{result}')