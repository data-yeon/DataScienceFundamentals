nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
print(f'nums: {nums}')
print(f'nums length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchResultIdx = -1

nums.append(searchData)

n = 0
while True:

    if nums[n] == searchData:
        if n != len(nums) - 1:
            searchResultIdx = n
        break

    n += 1

print(f'nums: {nums}')
print(f'nums length: {len(nums)}')
print(f'searchResultIdx: [{searchResultIdx}]')

if searchResultIdx < 0:
    print(f'찾으려는 {searchData}가(이) 없습니다.')
else:
    print(f'찾으려는 {searchData}의 위치(인덱스)는 {searchResultIdx}입니다.')