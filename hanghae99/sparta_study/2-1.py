def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # 숫자일 경우
            stack.append(int(token))
        else:  # 연산자일 경우
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # 정수 나눗셈

    return stack.pop()