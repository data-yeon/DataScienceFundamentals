n = int(input())  # 첫째 줄에 기록된 출입 기록의 수 n
logs = {}

# 출입기록
for _ in range(n):
    name, action = input().split()
    if action == "enter":
        logs[name] = True  # 회사에 들어오면 기록

    elif action == "leave":
        if name in logs:
            del logs[name]  # 회사에 나가면 기록 지우기
for name in sorted(logs.keys(), reverse=True):
    print(name)