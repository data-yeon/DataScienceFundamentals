from cProfile import label

import matplotlib.pyplot as plt

plt.title('plot #3')
plt.plot([1,2,3,4] , [2,4,6,8] , label= "even" )
plt.plot([1,2,3,4] , [1,3,5,7] , label= "odd" )
plt.legend()
plt.show()

# 데이터 획득
# 데이터 전처리
# 데이터 분리 : 훈련용, 검증용
# 모형 훈련
# 모형 검정
# 모형 적용