from importlib import import_module

import pandas as pd
import sklearn
from pandas.core.common import random_state
# from scipy.special import result

#   독립변수(입력): 범주형, 연속형. 종속변수(출력): 범주형 --> 독립변수를 연속형으로 변환 후 앙상블 기법 활용.

raw =  pd.read_csv('penguins.csv')
df = raw.copy()

print(df.head())
###################################
#   1-1. 데이터 전처리 - 결측치 처리
###################################

print(df.isna().sum())

# 행의 중앙값을 이용해 결측치를 처리한다
df['bill_length_mm'] = df['bill_length_mm'].fillna(df['bill_length_mm'].median())

df = df.dropna()
print(df.isna().sum())


###################################
#   1-2. 데이터 전처리 - 라벨 인코딩
###################################

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

label = ['sex']
for col in label:
    df[col] = le.fit_transform(df[col])



###################################
#   1-3. 데이터 전처리 - 더미변수 변환
###################################

dummies = ['island','sex']
print(df.dtypes)
for colum in dummies:
    df[colum] = df[colum].astype('category')

print(df.dtypes)

df = pd.get_dummies(df)
print(df.head()) # sex_0, sex_1 로 바꿔주는것

###################################
#   1-4. 데이터 전처리 - 정규화
###################################

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

target = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']

df[target] = scaler.fit_transform(df[target])

print(df.head())

###################################
#   1-5. 데이터 전처리 - 데이터 분리
###################################

import numpy as np
from sklearn.model_selection import train_test_split

# # 독립 변수 (X)와 종속 변수 (y) 분리
# X = df.iloc[:, 1:]  # 모든 열 중 1번째 열부터 마지막 열까지 (독립 변수)
# y = df.iloc[:, 0]   # 첫 번째 열 (종속 변수)
# 종속 변수를 이진 분류로 변환 (중앙값 기준)
# y = np.where(y > y.median(), 1, 0)
# 학습 데이터와 테스트 데이터 분리
xTrain, xTest, yTrain, yTest = train_test_split(df.iloc[:, 1:],  # 독립 변수 (1열부터 끝까지)
                                               df.iloc[:, 0],   # 종속 변수 (0번째 열)
                                               test_size=0.2, random_state=0)

# 결과 확인
print("Training set shape:", xTrain.shape, yTrain.shape)
print("Test set shape:", xTest.shape, yTest.shape)

###################################
#   2. 모형 훈련
###################################

from sklearn.ensemble import RandomForestClassifier

model1 = RandomForestClassifier()
model1.fit(xTrain, yTrain)
pred1 = model1.predict(xTest)
print(type(pred1))
# print(pred1)

from sklearn.ensemble import AdaBoostClassifier

model2 = AdaBoostClassifier()
model2.fit(xTrain, yTrain)
pred2 = model2.predict(xTest)

###################################
#   3. 모형 성능 검증
###################################

from sklearn.metrics import accuracy_score
acc1 = accuracy_score(yTest, pred1)
acc2 = accuracy_score(yTest, pred2)

print('acc1', acc1)
print('acc2', acc2)
###################################
#   4. 하이퍼 파라미터 최적화
###################################

#   ex.) number of perceptrons in neural net
#   ex.) number of estimators in randomforest
#   and so on

###################################
#   5. 결과 정리
###################################

result =le.inverse_transform(pred1)
print(result)

