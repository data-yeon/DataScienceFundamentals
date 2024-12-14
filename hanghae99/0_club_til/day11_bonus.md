

#### [비기너: 회사에 있는 사람, 해시](https://www.acmicpc.net/problem/7785)
#### [미들러: 빙산 / BFS](https://www.acmicpc.net/problem/2573)
#### [챌린저: 좌물쇠와 열쇠 / 기출](https://school.programmers.co.kr/learn/courses/30/lessons/60059)
### 비기너 
```python

n = int(input()) # 첫째 줄에 기록된 출입 기록의 수 n
logs = {}

# 출입기록 
for _ in range(n): 
    name, action = input().split()
    if action == "enter":
        logs[name] = True # 회사에 들어오면 기록
        
    elif action == "leave": 
        if name in logs:
            del logs[name]  # 회사에 나가면 기록 지우기 
for name in sorted(logs.keys(), reverse = True):
    print(name)
```

### 미들러 
