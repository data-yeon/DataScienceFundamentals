# 버블 정렬과는 반대라 볼 수 있다.
# 이미 정렬되어있는 부분에, 나 자신이 어디에 들어갈지를 판단해 삽입하는 것
# -> 정렬되어있는 자료 배열과 비교해서, 정렬 위치를 찾는다. 
import sortMod as sm
nums = [5, 10, 2, 1, 0]

# ascending
# for i1 in range(1, len(nums)):
#     i2 = i1 - 1
#     cNum = nums[i1]
#
#     while nums[i2] > cNum and i2 >= 0:
#         nums[i2 + 1] = nums[i2]
#         i2 -= 1
#
#     nums[i2+1] = cNum
#
#     print(f'nums: {nums}')

# nums = [0, 5, 2, 10, 1]
# descending
# for i1 in range(1, len(nums)):
#     i2 = i1 - 1
#     cNum = nums[i1]
#
#     while nums[i2] < cNum and i2 >= 0:
#         nums[i2 + 1] = nums[i2]
#         i2 -= 1
#
#     nums[i2+1] = cNum
#
#     print(f'nums: {nums}')


# sortMod 모듈
result = sm.sortNumber(nums, asc=False)
print(f'result: {result}')
