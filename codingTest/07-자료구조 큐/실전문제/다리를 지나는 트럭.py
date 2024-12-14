# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


# 트럭이 최대 올라갈 수 있는 대 수 : bridge_length
# 다리는 weight이하의 무게를 견딞 : weight
# truck_weights: 각 트럭의 무게
def solution(bridge_length, weight, truck_weights):
    dq = deque(truck_weights)
    current_truck_weights = 0  # 현재 다리에 오른 모든 트럭의 무게를 저장할 변수

    # 대기 트럭이 있는 동안
    while len(dq) > 0:
        current_truck_weights = dq.leftpop()
    return answer