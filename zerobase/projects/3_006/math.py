
# 최대공약수 유클리드 호제법

num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: ')) # 두번째 입력하는 수가 첫번째 입력하는 수보다 크다는 조건 ,

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0: # 공통된 약수 인 경우
        print('공약수: {}'.format(i))
        maxNum = i # 반복문 끝에 max Num 을 i로 할당

print('최대공약수: {}'.format(maxNum))