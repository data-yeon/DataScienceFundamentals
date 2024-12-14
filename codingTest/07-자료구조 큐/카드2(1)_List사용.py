
# O(n^2)   의 시간 복잡도를 가진다.
def solution(N : int) -> int:
    myQueue = []

    for i in range(1,N+1):
        myQueue.append(i)

    while len(myQueue) >1 :
        myQueue.pop(0) # 큐의 첫번째 요소를 제거 후,
        myQueue.append(myQueue.pop(0))    # 두번째 요소(첫번째 요소를 제거후 연속으로) 를 myQueue에 추가 \

    return myQueue[0]
if __name__ == '__main__':
    print(solution(6))