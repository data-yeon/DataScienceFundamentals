memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}

ks = memInfo.keys()
print(f'ks : {ks}')
print(f'ks type : {type(ks)}')

vs = memInfo.values()
print(f'vs : {vs}')
print(f'vs type : {type(vs)}')

items = memInfo.items()
print(f'items : {items}')
print(f'items type : {type(items)}')


ks = list(ks)
print(f'ks : {ks}')
print(f'ks type : {type(ks)}')

print(f'ks[0] : {ks[0]}')
print(f'ks[1] : {ks[1]}')
print(f'ks[2] : {ks[2]}')
print(f'ks[3] : {ks[3]}')


vs = list(vs)
print(f'vs : {vs}')
print(f'vs type : {type(vs)}')

print(f'vs[0] : {vs[0]}')
print(f'vs[1] : {vs[1]}')
print(f'vs[2] : {vs[2]}')
print(f'vs[3] : {vs[3]}')


items = list(items)
print(f'items : {items}')
print(f'items type : {type(items)}')

print(f'items[0] : {items[0]}')
print(f'items[1] : {items[1]}')
print(f'items[2] : {items[2]}')
print(f'items[3] : {items[3]}')


for key in ks:
    print(f'key: {key}')

for idx, key in enumerate(ks):
    print(f'idx, key: {idx}, {key}')

for value in vs:
    print(f'value: {value}')

for idx, value in enumerate(vs):
    print(f'idx, value: {idx}, {value}')

for item in items:
    print(f'item: {item}')

for idx, item in enumerate(items):
    print(f'idx, item: {idx}, {item}')

for key in memInfo.keys():
    print(f'{key}: {memInfo[key]}')



scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print(f'scores: {scores}')

minScore = 60
fStr = 'F(재시험)'
fDic = {}

for key in scores:
    if scores[key] < minScore:
        scores[key] = fStr
        fDic[key] = fStr

print(f'scores: {scores}')
print(f'fDic: {fDic}')
