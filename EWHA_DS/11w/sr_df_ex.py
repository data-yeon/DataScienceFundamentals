

import pandas as pd

nums = {"val" : [1,3,5,2,4,6], "alias": ['one',"three","five","two","four","six"]}

df = pd.DataFrame(nums)
# print(df)
# 2 차원의 표로 이루어진 데이터가 나온다.
print(df.head(5))

# Read
print(df["val"][0:2]) # 리스트가 꺼내어짐. 먼저 열을 지정한다음에, 열에서 행을 지정함.
print(df.loc[0:2, "val":"alias"])
print(df.iloc[0:2, 0:]) # 순서를 넣어주어야 함.  0: 끝까지~ 라는 의미이다. **교수님은 이걸 추천한대 (integer location)
print(df.iloc[-1,-1])                 # 추천하는 이유 1: -1 (맨끝의컬럼) 을 가져올수 있다.
                                     # 같의 상대적인 위치를 0,1,2.. 이런식으로 저장함.

# boolean indexing
# df[] 이 안에서 가져오겠다,
# 이 곽괄호 안에 조건을 지정해줘야 함. #

print(df[df.iloc[:,0] > 2])

# Update, - Append
nums2 = {"val" : [7,8] , "alias": ['seven', 'eight']}
df2 = pd.DataFrame(nums2)
print(df2)

df3 = pd.concat([df,df2]) # df에 df2를 붙여라
print(df3)

df4 = df3.reset_index()
print(df4)
df5 = df3.reset_index(drop=True)
print(df5) # 쓰지않는 Index를 없애줌

# 기존 데이터가 있다
# 기존 데이터에 이어붙일 데이터 프레임을 만든다
# 기존 데이터 프레임과 연결한다
# pandas -concat
# 새로 데이터 프레임을 만든다 df3= df1+df2
# append는 잘 쓰지않는다 . csv를 수정하고 빼고 넣고 그런거 하지않는다

df5.iloc[-1,1] = 'nine'
print(df5)

# Delete

df6= df5.drop([2,5]) # 2번째, 5번째 삭제
print(df6)

df7=df5.drop(columns=['alias'])
print('df : 컬럼(열)  alias삭제 ')
print(df7)

df8 = pd.read_csv('/Users/yeon/PycharmProjects/DataScienceFundamentals/EWHA_DS/11w/numbers.csv')
print(df8.head(5))

# map 사용  **꼭 알아야 함
def addOne(val):
    return val + 1
df9 =df8.map(addOne) # 각 셀에다가 주어진 함수의 연산을 해라
print(df9) # 각 데이터들을 하나하나 검사하고자 할때 함수를 만들어서 map을 사용 .


# apply 사용  ** 꼭 알아야 함.

def calcSum(nums):
    sum = 0
    for item in nums:
        sum += item
    return sum

df10 = df8.apply(calcSum)
print(df10) # 행이나 열 단위로 함수를 적용해준다 (**map과 다른점) 기본은 열 단위이다 (colum 값)

print(df8)
df11 = df8.apply(calcSum, axis=1) # 0
print(df11)