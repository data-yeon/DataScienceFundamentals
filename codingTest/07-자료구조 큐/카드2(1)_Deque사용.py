
# https://www.acmicpc.net/problem/2164
from collections import deque;

def solution( N: int ) -> int:
  myQueue = deque()

  for i in range(1, N+1):
    myQueue.append(i)
  while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft())
  return myQueue[0]

if __name__ == "__main__":
  print(solution(6)) # 4