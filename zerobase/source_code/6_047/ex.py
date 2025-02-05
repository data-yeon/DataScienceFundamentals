import random
import mergeAlgorithm

rNums = random.sample(range(1, 101), 20)

print(f'not sorted rNums: {rNums}')
print(f'merge sorted rNums by ASC: {mergeAlgorithm.mSort(rNums)}')
print(f'merge sorted rNums by DESC: {mergeAlgorithm.mSort(rNums, asc=False)}')