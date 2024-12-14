
import numpy as np

n = np.array([0,1,2,3,4,5])
print(n)
n = n.reshape([2,3])
print(n)


# Read 하는 방법

print(n[0,1])

print(n[0:2, 0:2])

# 0:2는 행 인덱스 범위 [0, 1]를 의미한다 (첫 번째와 두 번째 행 선택).
# 0:2는 열 인덱스 범위 [0, 1]를 의미한다 (첫 번째와 두 번째 열 선택).


print(n[n>=2])

# Update

n2 = np.array([6,7])
print(n2)
n2 = n2.reshape([2,1])
print(n2)
n3 = np.concatenate([n,n2],axis=1)
print(n3)
n3[1,2] = 9
print(n3)

# delete
n4 = np.delete(n3,[2,3],1 )
print(n4);

