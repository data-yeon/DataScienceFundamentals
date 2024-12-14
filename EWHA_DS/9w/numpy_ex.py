

import numpy as np


a1 = [1,3,5]
a2 = [2,4,6]

a3 = [a1, a2]
print(a3)

b1 = np.array(a3)
print(b1.shape) # 행렬의 모양을 말하는 중 (2행 3열)

b2 = b1.reshape([3,2]) # 3행 2열로 다시 만들어주는중
print(b2)
