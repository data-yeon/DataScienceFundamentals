# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    # 큐에 우선순위 와 인덱스 형태로 저장
    queue = deque((priority, index) for index, priority in enumerate(priorities))
    answer = 0  # 실행 순서를 기록할 변수
    while queue:
        current = queue.popleft()  # 큐의 맨 앞 프로세스를 꺼냄
        #  남아있는 프로세스 중 현재 프로세스보다 우선순위가 높은 프로세스가 있는지 확인
        # any(): 하나라도 조건을 만족하면 True 반환
        if (any(current[0] < process[0] for process in queue)):
            queue.append(current)
        else:
            # 우선순위가 가장 높으면 실행이 된다.
            answer += 1
            # 실행된 프로세스의 인덱스가 내가 찾는 프로세스의 인덱스(location)와 같은지 확인
            if current[1] == location:
                return answer
