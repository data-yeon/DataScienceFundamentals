friends = []

for i in range(5):
    friends.append(input('친구 이름 입력: '))

print(f'친구들 : {friends}')

friends.sort()
print(f'오름차순 : {friends}')

friends.sort(reverse=True)
print(f'내림차순 : {friends}')




numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'numbers : {numbers}')

for n in numbers:
    if numbers.count(n) >= 2:
        numbers.remove(n)

print(f'numbers : {numbers}')

