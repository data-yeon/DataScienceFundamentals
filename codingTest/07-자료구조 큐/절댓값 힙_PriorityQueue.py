# https://www.acmicpc.net/problem/11286

from queue import PriorityQueue

def solution(xlist : list) -> list:
    myQueue = PriorityQueue()
    answer = []

    for x in xlist:
        if x != 0:
            myQueue.put((abs(x), x))
        else:
            if myQueue.empty():
                answer.append(0)
            else:
                temp = myQueue.get()
                answer.append(temp[1])

    return answer
if __name__ == '__main__':
    # [-1, 1, 0, -1, -1, 1, 1, -2, 2, 0]
    print(solution([1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2,
0, 0, 0, 0, 0, 0, 0]))