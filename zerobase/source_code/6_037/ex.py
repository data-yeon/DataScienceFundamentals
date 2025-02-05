import random
import maxMod

if __name__ == '__main__':

    nums = []
    for n in range(30):
        nums.append(random.randint(1, 50))

    print(f'nums:\n{nums}')
    ma = maxMod.MaxAlgorithm(nums)
    print(f'max num: {ma.getMaxNum()}')
    print(f'max num cnt: {ma.getMaxNumCnt()}')