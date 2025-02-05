import random
import rankMod

if __name__ == '__main__':
    nums = random.sample(range(50, 101), 20)
    sNums = rankMod.rankAlgorithm(nums)
    print(f'sNums:\n{sNums}')

