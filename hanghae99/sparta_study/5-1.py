import heapq

# 무한대 비용 설정
INF = float('inf')


def dijkstra(n, graph, start, end):
    # 각 도시까지의 최소 비용을 무한대로 초기화
    distances = [INF] * (n + 1)
    distances[start] = 0

    # 우선순위 큐 설정
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (비용, 도시)

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        # 현재 도시의 거리보다 큰 비용이 큐에 들어온 경우 무시
        if current_distance > distances[current_city]:
            continue

        # 현재 도시와 연결된 모든 도시 탐색
        for adjacent, cost in graph[current_city]:
            new_distance = current_distance + cost

            # 새로운 비용이 기존 저장된 비용보다 작다면 업데이트
            if new_distance < distances[adjacent]:
                distances[adjacent] = new_distance
                heapq.heappush(priority_queue, (new_distance, adjacent))

    return distances[end]


def process_example(example_input):
    # 도시와 길 수 입력
    n = int(example_input[0])
    m = int(example_input[1])

    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]

    # 길 정보 입력
    for i in range(2, 2 + m):
        u, v, cost = map(int, example_input[i].split())
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    # 출발 도시와 도착 도시 입력
    start, end = map(int, example_input[2 + m].split())

    # 최소 비용 계산 및 출력
    minimum_cost = dijkstra(n, graph, start, end)
    print(f"출발 도시 {start}에서 도착 도시 {end}로 가는 최소 비용은 {minimum_cost}입니다.")


# 예시 입력 설정
example_input_1 = [
    "4",
    "5",
    "1 2 4",
    "1 3 2",
    "2 3 5",
    "2 4 1",
    "3 4 7",
    "1 4"
]

example_input_2 = [
    "5",
    "7",
    "1 2 3",
    "1 3 4",
    "2 3 1",
    "2 4 6",
    "3 4 5",
    "3 5 2",
    "4 5 4",
    "1 5"
]

# 예시 실행
print("첫 번째 예시 결과:")
process_example(example_input_1)

print("\n두 번째 예시 결과:")
process_example(example_input_2)