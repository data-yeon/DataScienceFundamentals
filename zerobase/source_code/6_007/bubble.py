# 버블정렬 :  처음부터 끝까지 인접하는 인덱스의 값을 순차적으로 비교하며 큰 숫자를 가장 끝으로 옮기는 알고리즘.

nums = [10, 2, 7, 21, 0]
# print(f'not sorted nums: {nums}')

length = len(nums) - 1
for i in range(length):
    for j in range(length-i):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            # nums[j], nums[j+1] = nums[j+1], nums[j]
            # 파이썬에서 자리 바꾸는 법

        print(nums)
    print()

print(f'sorted nums: {nums}')

# import copy
#
# def bubbleSort(ns):
#     cns = copy.copy(ns)
#     length = len(cns) - 1
#     for i in range(length):
#         for j in range(length - i):
#             if cns[j] > cns[j + 1]:
#                 cns[j], cns[j + 1] = cns[j + 1], cns[j]
#
#     return cns
#
# nums = [10, 2, 7, 21, 0]
# sortedNums = bubbleSort(nums)
#
# print(f'nums: {nums}')
# print(f'sortedNums: {sortedNums}')

