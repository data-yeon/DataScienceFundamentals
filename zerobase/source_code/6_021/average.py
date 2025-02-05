import random

nums = random.sample(range(0, 100), 30)
print(f'nums: {nums}')

total = 0
for n in nums:
    total += n

average = total / len(nums)
print(f'average: {round(average, 2)}')


# 50이상 90이하 수들의 평균
import random

nums = random.sample(range(0, 100), 30)
print(f'nums: {nums}')

targetNums = []
total = 0
for n in nums:
    if n >= 50 and n <= 90:
        total += n
        targetNums.append(n)

print(f'targetNums: {targetNums}')
average = total / len(targetNums)
print(f'average: {round(average, 2)}')


# 정수들의 평균
nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
print(f'nums: {nums}')

targetNums = []
total = 0
for n in nums:
    if n - int(n) == 0:
        total += n
        targetNums.append(n)

print(f'targetNums: {targetNums}')
average = total / len(targetNums)
print(f'average: {round(average, 2)}')


# 실수(소수)들의 평균
nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
print(f'nums: {nums}')

targetNums = []
total = 0
for n in nums:
    if n - int(n) != 0:
        total += n
        targetNums.append(n)

print(f'targetNums: {targetNums}')
average = total / len(targetNums)
print(f'average: {round(average, 2)}')


