from collections import deque

def escape_maze(maze):
    # 미로의 크기를 구합니다
    n = len(maze)
    m = len(maze[0])

    # 상하좌우 이동 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS를 위한 큐 초기화, 시작 위치 (0, 0)과 거리 1을 큐에 추가
    queue = deque([(0, 0, 1)])  # (x, y, distance)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 출구에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist

        # 상하좌우로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 이동 가능한 범위인지 확인하고 방문하지 않은 경로라면 이동
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1  # 출구에 도달할 수 없을 경우

# 예제 입력
maze = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

# 함수 호출
print(escape_maze(maze))  # 예시 출력: 8