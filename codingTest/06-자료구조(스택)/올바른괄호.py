# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()  # () 쌍이 맞으면 추가 없이 스택에서 제거
            else:
                return False  # 스택이비었는데 닫는괄호가 나옴
    return not stack  # 스택이 비어있으면 True, 아니면 False


# 테스트 코드
def test_solution():
    test_cases = [
        ("()", True),
        ("(())", True),
        ("()()", True),
        ("(()())", True),
        ("", True),
        ("(", False),
        (")", False),
        ("(()", False),
        ("())", False),
        ("()(", False),
        ("())(()", False),
        ("(()(()))", True),
        ("((())())", True),
        ("(()()(()))", True),
        ("((())", False),
        (")(", False),
        (")()(", False),
        ("()()()()", True),
        ("(((((())))))", True),
        ("(((((())))))(", False),
    ]

    for idx, (input_str, expected_output) in enumerate(test_cases, 1):
        result = solution(input_str)
        print(
            f"테스트 케이스 {idx}: 입력값: '{input_str}' | 예상 결과: {expected_output} | 실행 결과: {result} | {'통과' if result == expected_output else '실패'}")


# 테스트 코드 실행
test_solution()