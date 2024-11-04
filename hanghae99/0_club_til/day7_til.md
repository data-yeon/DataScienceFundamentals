### 근무 지옥에 빠진 푸앙이 (Small)
![hanghae Logo](https://hanghae99.spartacodingclub.kr/_next/image?url=https%3A%2F%2Fstatic.spartacodingclub.kr%2Fhanghae99%2F99club%2Fproblems%2Fcoding-test-til.png&w=640&q=75)
#### [백준링크](https://www.acmicpc.net/problem/25593)

### 99클럽 코테 스터디 7일차 TIL + 해시맵, 시간 복잡도, 투 포인터
```python
def calculate_work_hours(schedule, time_slots):
    work_hours = {}
    
    for day in schedule:
        for i, shift in enumerate(day):
            hours = time_slots[i]
            for name in shift:
                if name != '-':
                    if name in work_hours:
                        work_hours[name] += hours
                    else:
                        work_hours[name] = hours
    return work_hours

def is_fair_schedule(work_hours):
    if not work_hours:  # 근무자가 없으면 공평하다고 간주
        return "Yes"
    
    max_hours = max(work_hours.values())
    min_hours = min(work_hours.values())
    
    return "Yes" if max_hours - min_hours <= 12 else "No"

# 입력 처리
n = int(input().strip())
schedule = []

# 시간대별 근무 시간
time_slots = [4, 6, 4, 10]

for _ in range(n):
    week_schedule = []
    for _ in range(4):
        # 각 시간대 근무자를 리스트로 추가
        shift = input().strip().split()
        week_schedule.append(shift)
    schedule.append(week_schedule)

# 전체 근무 시간 계산
work_hours = calculate_work_hours(schedule, time_slots)

# 공평성 확인 후 출력
result = is_fair_schedule(work_hours)
print(result)
```

## 오늘의 학습 키워드
- 해시맵(HashMap)
- 시간복잡도(Time Complexity)
- 문제 해결 패턴 (투포인터, 슬라이딩 윈도우 등)

## 공부한 내용 본인의 언어로 정리하기
오늘은 **해시맵**에 대해 학습했다. 해시맵은 키-값 쌍을 저장하는 데이터 구조로, 빠른 검색과 삽입을 위해 사용된다. 이를 통해 데이터를 O(1) 시간복잡도로 접근할 수 있어 많은 코딩 테스트 문제에서 유용하게 사용된다.

## 오늘의 회고
- **어떤 문제가 있었고, 나는 어떤 시도를 했는지**  
  해시맵을 사용하는 문제에서 중복 키를 처리하는 방법이 헷갈렸다. 여러 시도를 통해 값을 업데이트하는 방식과 새로운 키를 추가하는 방식을 분리하여 접근하려고 했다.

- **어떻게 해결했는지**  
  예제 코드를 분석하고 직접 디버깅하면서 중복 키 발생 시 기존 값을 업데이트하는 로직을 성공적으로 구현했다.

- **무엇을 새롭게 알았는지**  
  해시맵을 사용할 때, 존재하지 않는 키에 접근하려고 하면 오류가 발생하므로 `if` 조건문으로 미리 확인하는 습관이 필요하다는 것을 알게 되었다.

- **내일 학습할 것은 무엇인지**  
  내일은 시간복잡도에 대한 이해를 심화하고, 해시맵을 응용한 문제를 더 풀어볼 계획이다.

---

#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL