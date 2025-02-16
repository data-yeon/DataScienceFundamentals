# 근삿값
import random  # 랜덤 숫자를 생성하기 위한 random 모듈 불러오기

# 0부터 49까지의 숫자 중에서 20개의 서로 다른 숫자를 랜덤하게 선택하여 리스트로 생성
nums = random.sample(range(0, 50), 20)  
print(f'nums: {nums}')  # 생성된 랜덤 숫자 리스트 출력

# 사용자로부터 입력을 받아 정수형(int)으로 변환
inputNum = int(input('input number: '))  
print(f'inputNum: {inputNum}')  # 사용자가 입력한 숫자 출력

# 근삿값을 저장할 변수 nearNum을 0으로 초기화
nearNum = 0  

# 최소 차이값(최소 절댓값 차이)을 저장할 변수 minNum을 50으로 초기화
# (0~49 사이의 숫자를 다루므로 초기값을 50으로 설정하여 비교할 때 더 작은 값이 나오도록 함)
minNum = 50  

# 리스트에 있는 숫자들을 하나씩 확인하며 근삿값을 찾음
for n in nums:
    absNum = abs(n - inputNum)  # 현재 숫자(n)와 입력값(inputNum)의 차이의 절댓값 계산
    # print(f'absNum: {absNum}')  # 절댓값 차이를 확인하는 디버깅용 출력 (주석 처리 가능)

    # 만약 현재 숫자의 절댓값 차이가 minNum보다 작다면, 더 가까운 숫자로 업데이트
    if absNum < minNum:
        minNum = absNum  # 최소 차이값(minNum) 업데이트
        nearNum = n  # 가장 가까운 숫자(nearNum)도 업데이트

# 최종적으로 입력값과 가장 가까운 숫자 출력
print(f'nearNum: {nearNum}')  