def solution(nums):
    unique_types = len(set(nums))  # 고유한 폰켓몬 종류 수
    max_selection = len(nums) // 2  # 선택할 수 있는 최대 폰켓몬 수

    # 최종 선택할 수 있는 폰켓몬 종류의 최대 개수 반환
    return min(unique_types, max_selection)

print(solution([3, 1, 2, 3]))  # 결과: 2
print(solution([3, 3, 3, 2, 2, 4]))  # 결과: 3
print(solution([3, 3, 3, 3, 3, 3]))  # 결과: 1