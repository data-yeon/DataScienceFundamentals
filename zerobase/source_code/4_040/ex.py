import random

randomList = random.sample(range(1, 101), 10)
evens = []
odds = []

for n in randomList:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(f'짝수: {evens}, 개수: {len(evens)}개')
print(f'홀수: {odds}, 개수: {len(odds)}개')


