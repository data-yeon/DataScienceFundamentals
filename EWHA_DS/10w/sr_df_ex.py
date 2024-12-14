

import pandas as pd

sr = pd.Series([0,1,2,3,4,5]);
print(sr)
print(sr.index)
print(sr.values)

# Read
print("Read")
print(sr[1])
print(sr[1:3])

# sr.loc

print("sr.loc()")
print(sr.loc[1])
print(sr.loc[1:3])

sr2 = pd.Series(['a','b','c','d','e','f'],  index=['i1', 'i2', 'i3', 'i4', 'i5', 'i6'])

print(sr2.loc['i1'])
print(sr2.loc['i3'])

print(sr2[sr2 >='c'])
print(sr2[sr2.iloc[:] >='c'])

# Update
print(sr2)
sr3 = pd.Series(['g','h'])
sr4 = pd.concat([sr2,sr3])
print(sr4) # 그냥 이렇게 하면 인덱스가 다 틀어져 버린다.
# sr4 = sr4.reset_index(drop=False) ## drop = false하면 기존 인덱스를 살린다.
sr4 = sr4.reset_index(drop=True)
print(sr4)
# print(sr5)

sr4.iloc[-1] =  10
print(sr4)
# delete
sr6= sr4.drop(['i1', 'i3']) # reset index 를 지우고 해야 함.
print(sr6)