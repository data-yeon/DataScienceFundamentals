def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # 모든 원소에 대해 부분 수열의 최소 길이는 1로 초기화

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# 예시 입력
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 출력: 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))            # 출력: 4