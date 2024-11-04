
samples = [1,3,5,7,9,11]
sum = 0

# for sample in samples:
#     sum += sample
sample2 = [0,2,4,6,8,10]

# for sample2 in sample2:
#     sum += sample2

def calcSum(inputList):
    sum = 0
    for sample in inputList:
        sum += sample

        return sum

sum = calcSum(samples)

# 코드 재활용 관점 (위)


# 빌딩 블록으로 사용 (아래)
def calcAverage(samples):
    # 합을 계산한다.
    sum = calcSum(samples)
    # 원소의 갯수를 구한다.
    length = calcLen(samples)
    # 결과를 알려준다.
    avg = sum/length
    return sum

samples = [1,3,5,7,9,11]
sum = None
sum = calcSum(samples)

