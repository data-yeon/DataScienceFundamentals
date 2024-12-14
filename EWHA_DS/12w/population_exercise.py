import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.family'] ='NanumGothic'  # for displaying Hangul
# plt.rcParams['font.family'] ='AppleGothic'  # for displaying Hangul for Mac


##############################################################################
#
#   0. 데이터 읽어오기
#
##############################################################################

encoding = 'EUC-KR'


##############################################################################
#
#   1. 데이터 전처리(pre-processing)
#
##############################################################################

#   원본 데이터에서 제목, 총합, 평균 등 필요없는 데이터를 빼고 분석 대상이 될 데이터만 가져옵니다.
#   만약 값이 입력되어 있지 않은 셀 등이 있으면(결측치, missing values), 평균, 중간값 등으로 채워주어야 하는 경우도 있습니다.


#   결측값 처리

def convertStrToInt(strInt):
    if not isinstance(strInt, int):
        result = int(strInt.replace(',', ''))
    else:
        result = strInt

    return result


#   라벨 인코딩

#   더미변수 처리

#   데이터 분리


##############################################################################
#
#   2. 모형 개발, 적용, 평가
#
##############################################################################

#   모형 개발
def calcRMSE(tar, ref): # calculate RMSE(Root Mean Square Error)

    RMSE = None   # initial value

    accSquareError = 0.0   # accumulated square error with initial value 0

    if len(tar) != len(ref):
        pass
    else:
        if len(tar) == 0 or len(ref) == 0:
            pass
        else:
            for idx in range(len(ref)):
                error = tar[idx] - ref[idx]
                squareError = error*error
                accSquareError = accSquareError + squareError
            meanSquareError = accSquareError/len(ref)
            RMSE = np.sqrt(meanSquareError)

    return RMSE

#   모형 훈련(모형 적용)

#   나의 동네 인구구성 찾고 읽기
#   전처리를 마친 데이터에서 행정 구역명(예) myHomeTown = '남구 효곡동')을 기준으로 내가 살고 있는 동네 인구구성이 들어있는 행을 찾습니다.
#   찾은 행에서 행정 구역명을 제외한 인구구성 데이터만 가져와 변수에 저장합니다.
#   인구구성 데이터만 가지고 있어야 다른 동네 인구구성 데이터와 비교할 수 있기 때문입니다.


#   모형 적용 - 인구구성 데이터 비교하기
#   위 '나의 동네 인구구성 찾고 읽기' 과정에서 얻은 내가 사는 동네 인구구성 데이터와 다른 동네들의 인구구성을 비교해줍니다.
#   인구 구성이 얼마나 비슷한지 최소자승오차(RMSE) 개념을 이용하여 그 오차를 수치로 측정해줍니다.
#   이 최소자승오차가 가장 작은 동네를 찾으면 이 동네가 우리 동네와 인구구성이 가장 비슷한 동네입니다. 찾은 동네를 변수에 저장해줍니다.



##############################################################################
# 
#   3. 결과 정리
# 
##############################################################################

#   인구구성 데이터 시각화
#   위 과정에서 찾은 '내가 살고 있는 동네'와 '인구구성이 가장 비슷한 동네'의 인구구성을 그래프로 나타내줍니다.
#   시각화를 통해 그 결과가 얼마나 유사한지 직접 확인해 볼 수 있습니다.

