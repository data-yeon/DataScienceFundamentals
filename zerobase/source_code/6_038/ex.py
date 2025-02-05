import random
import minMod

if __name__ == '__main__':

    nums = []
    for n in range(30):
        nums.append(random.randint(1, 50))

    print(f'nums:\n{nums}')
    ma = minMod.MinAlgorithm(nums)
    print(f'min num: {ma.getMinNum()}')
    print(f'min num cnt: {ma.getMinNumCnt()}')