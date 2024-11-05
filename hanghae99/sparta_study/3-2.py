def generate_permutations(arr):
    result = []
    visited = [False] * len(arr)

    def backtrack(current_permutation):
        # 현재 순열이 주어진 배열과 길이가 같다면 결과에 추가
        if len(current_permutation) == len(arr):
            result.append(current_permutation[:])
            return

        for i in range(len(arr)):
            # 이미 사용한 숫자는 건너뜀
            if visited[i]:
                continue

            # 숫자를 추가하고 방문 체크
            visited[i] = True
            current_permutation.append(arr[i])

            # 재귀 호출
            backtrack(current_permutation)

            # 백트래킹: 마지막에 추가한 숫자 제거 및 방문 해제
            current_permutation.pop()
            visited[i] = False

    # 백트래킹 시작
    backtrack([])
    return result

# 예제 입력
arr = [1, 2, 3]

# 함수 호출
permutations = generate_permutations(arr)
for p in permutations:
    print(p)