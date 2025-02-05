sports = ['농구', '수구', '축구', '마라톤', '테니스']

for i in range(len(sports)):
    print('{} : {}'.format(i, sports[i]))

for idx, value in enumerate(sports):
    print('{} : {}'.format(idx, value))


str = 'Hello python.'
for idx, value in enumerate(str):
    print('{} : {}'.format(idx, value))



sports = ['농구', '수구', '축구', '마라톤', '테니스']
favoriteSport = input('가장 좋아하는 스포츠 입력: ')

bestSportIdx = 0
for idx, value in enumerate(sports):
    if value == favoriteSport:
        bestSportIdx = idx + 1

print('{}(은)는 {}몇 번째에 있습니다.'.format(favoriteSport, bestSportIdx))



message = input('메시지 입력: ')
cnt = 0
for idx, value in enumerate(message):
    if value == ' ':
        cnt += 1

print('공백 개수 : {}'.format(cnt))