# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    left = 0  # 왼쪽 포인터 초기화
    min_len = len(gems)  # 최소 구간 길이를 gems의 길이로 초기화
    buy = []  # 현재 보석 구간을 저장하는 리스트 (슬라이딩 윈도우)
    result = [1, len(gems)]  # 정답 구간의 시작과 끝을 저장하는 리스트
    num = set()  # 구해야 하는 보석 종류를 저장하는 set
    for gem in gems:
        num.add(gem) # 중복 없이 유니크하게 보석 종류만 남는다.
    for right in range(len(gems)):
        buy.append(gems[right]) # 오른쪽 포인터의 보석을 현재 구간에 추가
        while all(gem in buy for gem in num):
            # all() 모든 조건이 참인지를 확인,
            #  현재 구간 buy가 모든 보석 종류를 포함하는지 확인하는 부분이다.
            if min_len > len(buy): # 더 짧은 구간이 발견되면 업데이트
                min_len = len(buy)
                result = [left+1, right+1] # 인덱스 1 부터 시작하도록 조정
            left += 1 # 왼쪽 포인터 이동
            buy.pop(0) # 현재 구간에서 가장 왼쪽 보석 제거 
    return result