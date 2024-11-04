#######################################################################################
#
#   1. 두 수를 입력으로 받고 이 중 큰 수를 반환하는 기능을 제공하는 함수를 작성하시오.
#
#######################################################################################
a = int(input("a 값을 입력하시오: "))
b = int(input("b 값을 입력하시오: "))

def getLargerOne(a, b):
    # 함수의 내용(body)을 작성하시오.
    if a > b:
        return a
    elif b > a:
        return b
    else:
        print("a와 b 값이 같습니다.")
        return None  # 두 값이 같을 때 None을 반환하거나 필요에 따라 다른 처리를 할 수 있음

result = getLargerOne(a, b)
if result is not None:
    print(f"더 큰 값은: {result}")