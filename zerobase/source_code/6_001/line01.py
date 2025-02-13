# 선형검색
# 일렬로 나열된 곳에서 데이터를 찾는다.
# 선형으로 나열되어 있는 데이터를 순차적으로 스캔하면서 원하는 값을 찾는다.

# 보초법 :
# 마지막 인덱스에 찾으려는 값을 임의로 추가해서 찾는 과정을 간략화 한다.
 # 검색성공 : 마지막 이전에 찾는 숫자가 있다.
 # 검색실패 : 마지막에 찾는 숫자가 검색된 경우
datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

n = 0
while True:

    if n == len(datas):
        searchResultIdx = -1
        break

    elif datas[n] == searchData:
        searchResultIdx = n
        break

    n += 1

print(f'searchResultIdx: [{searchResultIdx}]')

