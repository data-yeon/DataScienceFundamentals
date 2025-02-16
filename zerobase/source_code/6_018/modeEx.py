import random  # 랜덤 모듈 불러오기
import maxScore as ms  # maxScore 모듈을 ms로 임포트

scores = []  # 점수를 저장할 리스트

# 100개의 랜덤 점수 생성
for i in range(100):
    rn = random.randint(71, 100)  # 71에서 100 사이의 랜덤 정수 생성
    if rn != 100:  # 100이 아닐 경우, 5의 배수로 맞춤
        rn = rn - (rn % 5)  # 예: 78 → 75, 83 → 80
    scores.append(rn)  # 변환된 점수를 리스트에 추가

print(f'scores: {scores}')  # 생성된 점수 리스트 출력
print(f'scores length: {len(scores)}')  # 점수 리스트의 길이 출력 (100개여야 함)

# 최댓값 찾기 알고리즘 사용
maxAlo = ms.MaxAlgorithm(scores)  # 점수 리스트를 MaxAlgorithm 클래스에 전달
maxAlo.setMaxIdxAndNum()  # 최댓값과 해당 인덱스를 설정
maxNum = maxAlo.getMaxNum()  # 최댓값 가져오기
print(f'maxNum: {maxNum}')  # 최댓값 출력

# 최댓값을 기준으로 인덱스 리스트 생성 (빈도수를 저장할 리스트)
indexes = [0 for i in range(maxNum + 1)]  # 최댓값 + 1 크기의 리스트 생성 (모든 점수의 빈도수를 저장)
print(f'indexes: {indexes}')  # 초기화된 인덱스 리스트 출력
print(f'indexes length: {len(indexes)}')  # 인덱스 리스트의 길이 출력

# 각 점수의 빈도수를 indexes 리스트에 저장
for n in scores:
    indexes[n] = indexes[n] + 1  # 점수에 해당하는 위치의 값을 1 증가 (빈도수 누적)
print(f'indexes: {indexes}')  # 빈도수가 저장된 인덱스 리스트 출력

n = 1  # 출력 순서 번호

# 빈도수가 가장 높은 점수를 찾고 출력하는 반복문
while True:
    maxAlo = ms.MaxAlgorithm(indexes)  # indexes 리스트를 MaxAlgorithm 클래스에 전달
    maxAlo.setMaxIdxAndNum()  # 최댓값과 해당 인덱스를 설정
    maxNum = maxAlo.getMaxNum()  # 가장 많이 등장한 점수의 빈도수 가져오기
    maxNumIdx = maxAlo.getMaxNumIdx()  # 가장 많이 등장한 점수의 값(점수) 가져오기

    if maxNum == 0:  # 빈도수가 0이면 더 이상 출력할 점수가 없으므로 반복 종료
        break

    print(f'{n}. {maxNumIdx}빈도수: {maxNum}\t', end='')  # 현재 빈도수가 가장 높은 점수와 빈도수 출력
    print('+' * maxNum)  # 빈도수만큼 "+" 출력하여 시각적으로 표현
    indexes[maxNumIdx] = 0  # 현재 출력한 점수의 빈도수를 0으로 설정하여 다음 최대 빈도수를 찾을 수 있도록 함

    n += 1  # 출력 순서 증가