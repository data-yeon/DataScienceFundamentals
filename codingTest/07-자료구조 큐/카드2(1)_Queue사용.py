from queue import Queue

def solution(N: int) -> int:
    myQueue = Queue()

    for i in range(1, N + 1):
        myQueue.put(i)

    while myQueue.qsize() > 1:
        myQueue.get() # 큐의 첫번째 요소 제거
        myQueue.put(myQueue.get()) # 그 다음 요소 맨 아래로 이동

    return myQueue.get()

if __name__ == '__main__':
    print(solution(6))
