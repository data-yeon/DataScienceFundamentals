#######################################################################################
#
#   1. 두 수를 입력으로 받고 이 중 큰 수를 반환하는 기능을 제공하는 함수를 작성하시오.
#
#######################################################################################

def getLargerOne(a, b):
    # 함수의 내용(body)을 작성하시오.
    # a = input("a 값 을 입력하시오: ")
    # b = input("b 값 을 입력하시오: ")
    # if a > b:
    #     return a
    # elif  b > a:
    #     return b
    # else:
    #     print("a, b값이 같습니다. ")




#######################################################################################
#
#   2. 아래 calcSum() 함수는 주어진 리스트의 합(sum)을 구하는 함수입니다.
#   이 함수를 이용해서 sample 리스트의 평균을 구하는 함수 calcAverage()를 완성하시오.
#
#######################################################################################

def calcSum(inputList):
    sum = 0

    for item in inputList:
        sum = sum + item

    return sum

sample = [-8, 2, 12, 17, 21, 25, 28, 23, 19, 12, 8, -5]

def calcAverage(inputList):
    avg = None 

    #   함수를 완성 하시오.

    return avg


#######################################################################################
#
#   3. 아래는 5개 도시의 월 평균 기온입니다.
#   도시 각각의 연평균 기온을 구한 후 cityTempAvg 리스트에 저장하시오.
#
#######################################################################################

cityTempDict = {}   #   5개 도시의 월 평균 기온들을 보관하는 딕셔너리

cityTempDict['서울'] = [-8, -4, 7, 13, 21, 29, 32, 33, 27, 19, 8, -5]
cityTempDict['춘천'] = [-14, -9, 3, 9, 19, 26, 31, 32, 24, 13, 2, -9]
cityTempDict['청주'] = [-5, -3, 9, 15, 23, 28, 30, 32, 29, 20, 12, -4]
cityTempDict['광주'] = [-5, -1, 8, 17, 23, 29, 32, 33, 25, 15, 6, -3]
cityTempDict['포항'] = [-4, 3, 12, 16, 24, 30, 33, 34, 28, 22, 11, -3]

cityTempAvg = []    #   5개 도시 각각의 연 평균 기온을 저장할 리스트

for key in cityTempDict.keys():
    #   각 도시의 연 평균 기온을 구한 후 cityTempAvg 리스트에 저장하시오.


print(cityTempAvg)  # 결과 확인


#######################################################################################
#
#   4. 문제 3에서 구한 연 평균 기온(cityTempAvg) 중 최대값을 찾는 프로그램을 
#   max() 함수를 사용하지 말고 작성하시오.
#
#######################################################################################

maxVal = cityTempAvg[0]

for item in cityTempAvg:
    if item > maxVal:

    else:


print(maxVal)   # 결과 확인


#######################################################################################
#
#   5. 입력으로 주어진 리스트에서 최대값을 찾는 함수를 max() 함수를 사용하지 말고 작성하시오.
#
#######################################################################################

def getMaxValue(inputList):

    #   입력으로 주어진 리스트에서 최대값을 찾는 코드를 작성하시오.

    return maxVal

print(maxVal)
