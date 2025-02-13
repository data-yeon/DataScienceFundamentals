# 이진검색
# 정렬이 되어있는 자료 구조에서 중앙값과의 크고 작음을 이용해 데이터를 검색한다.
# 정렬이 된 데이터에서, 가운데 값을 구해서. 크냐 작으냐에 따라서 숫자를 버려버림, 검색 범위를 점차 좁혀나가면서
# 내가 원하는 데이터를 찾아나가는 방식

#       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# datas = [1, 3, 4, 6, 7, 8, 9, 11]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

staIdx = 0
endIdx = len(datas) - 1
midIdx = (staIdx +  endIdx) // 2
midVal = datas[midIdx]
print(f'midIdx: {midIdx}')
print(f'midVal: {midVal}')

while searchData <= datas[len(datas)-1] and searchData >= datas[0]:

    if searchData == datas[len(datas)-1]:
        searchResultIdx = len(datas)-1
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: [{searchResultIdx}]')

