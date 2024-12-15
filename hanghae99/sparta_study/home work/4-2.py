def max_meetings(meetings):
    # 종료 시간을 기준으로 회의 목록을 정렬
    # 이렇게 정렬하면 가장 먼저 종료되는 회의부터 선택할 수 있게 되어 최적의 회의 수를 배정할 수 있음
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    # 첫 번째 회의를 선택하는 것으로 시작하며, 회의 수를 1로 초기화
    count = 1
    # 첫 번째 선택된 회의의 종료 시간을 기준으로 삼음
    last_end_time = sorted_meetings[0][1]

    # 정렬된 회의 목록을 두 번째 회의부터 순회
    for i in range(1, len(sorted_meetings)):
        # 현재 회의의 시작 시간과 종료 시간을 가져옴
        start, end = sorted_meetings[i]

        # 현재 회의의 시작 시간이 이전 선택된 회의의 종료 시간 이후라면, 회의가 겹치지 않으므로 선택 가능
        if start >= last_end_time:
            # 회의를 선택했으므로 회의 수를 증가
            count += 1
            # 마지막 선택된 회의의 종료 시간을 현재 회의의 종료 시간으로 갱신
            last_end_time = end

    # 최대 선택 가능한 회의 수 반환
    return count

# 테스트 예시
meetings1 = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
print(max_meetings(meetings1))  # 출력: 3,

meetings2 = [(1, 3), (2, 4), (5, 8), (6, 10), (8, 11), (10, 12)]
print(max_meetings(meetings2))  # 출력: 3,