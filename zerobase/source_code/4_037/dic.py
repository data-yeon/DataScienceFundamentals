memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}
print(f'memInfo: {memInfo}')

del memInfo['메일']
print(f'memInfo: {memInfo}')

del memInfo['취미']
print(f'memInfo: {memInfo}')



memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}
print(f'memInfo: {memInfo}')

returnValue = memInfo.pop('이름')
print(f'memInfo: {memInfo}')
print(f'returnValue: {returnValue}')
print(f'returnValue type: {type(returnValue)}')

returnValue = memInfo.pop('취미')
print(f'memInfo: {memInfo}')
print(f'returnValue: {returnValue}')
print(f'returnValue type: {type(returnValue)}')




scores = {'score1':8.9, 'score2':8.1, 'score3':8.5, 'score4':9.8, 'score5':8.8}
minScore = 10; minScoreKey = ''
maxScore = 0; maxScoreKey = ''

for key in scores.keys():
    if scores[key] < minScore:
        minScore = scores[key]
        minScoreKey = key

    if scores[key] > maxScore:
        maxScore = scores[key]
        maxScoreKey = key

print('minScore : {}'.format(minScore))
print('minScoreKey : {}'.format(minScoreKey))

print('maxScore : {}'.format(maxScore))
print('maxScoreKey : {}'.format(maxScoreKey))

del scores[minScoreKey]
del scores[maxScoreKey]

print('scores : {}'.format(scores))