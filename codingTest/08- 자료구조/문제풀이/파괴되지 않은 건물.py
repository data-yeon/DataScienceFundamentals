# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    result= 0
    m = len(board[0])
    n = len(board)

    # 초기값을 0 으로 채운 attack 행렬을 만든다.
    attack = [[0 for _ in range(m+1)] for __ in range(n+1)]
    for type, r1,c1,r2,c2,degree in skill:
        deal = degree if type == 2 else -degree
        # type :1 (공격), 감소, 2: 회복 (증가)
        attack[r1][c1] += deal # (r1, c1)에서 deal만큼 시작점에 더한다.
        attack[r1][c2+1] -= deal # (r1, c2+1)에서 deal만큼 뺀다 → 같은 행에서 오른쪽 끝이 끝남을 나타냄.
        attack[r2+1][c1] -= deal # (r2+1, c1)에서 deal만큼 뺀다 → 같은 열에서 아래 끝이 끝남을 나타냄.
        attack[r2+1][c2+1] += deal # (r2+1, c2+1)에서 deal만큼 다시 더한다 → 중복된 부분을 보정한다.
    for i in range(n) :
        # 누적합 계산 (가로)
        for j in range(m) :
            attack[i][j+1] += attack[i][j]
    for j in range(m) :
        # 누적합 계산 (세로)
        for i in range(n) :
            attack[i+1][j] += attack[i][j]
    for i in range(n) :
        # board에 누적합 적용 및 남아있는 건물 개수 카운트
        for j in range(m) :
            board[i][j] += attack[i][j]
            if board[i][j] > 0 :
                result += 1
    return result

solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]])