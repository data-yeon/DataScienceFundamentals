myInfo = {}

myInfo['이름'] = '박경진'
myInfo['전공'] = 'computer'
myInfo['메일'] = 'jin@naver.com'
myInfo['학년'] = 3
myInfo['주소'] = '대한민국 서울'
myInfo['취미'] = ['요리', '여행']

print(f'myInfo : {myInfo}')

myInfo['전공'] = 'sports'
myInfo['학년'] = '4'
print(f'myInfo : {myInfo}')


scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print(f'scores : {scores}')

minScore = 60
fStr = 'F(재시험)'
if scores['kor'] < minScore: scores['kor'] = fStr
if scores['eng'] < minScore: scores['eng'] = fStr
if scores['mat'] < minScore: scores['mat'] = fStr
if scores['sci'] < minScore: scores['sci'] = fStr
if scores['his'] < minScore: scores['his'] = fStr
print(f'scores : {scores}')


# 키 / (신장 * 신장)
myBodyInfo = {'이름':'gildong', '몸무게':83.0, '신장':1.8}
myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)
print(f'myBodyInfo: {myBodyInfo}')
print(f'myBMI: {round(myBMI, 2)}')

date = 0
while True:
    date += 1
    myBodyInfo['몸무게'] = round((myBodyInfo['몸무게'] - 0.3), 2)
    print('몸무게: ', myBodyInfo['몸무게'])
    myBodyInfo['신장'] = round((myBodyInfo['신장'] + 0.001), 3)
    print('신장: ', myBodyInfo['신장'])
    myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)

    if date >= 30:
            break

print(f'myBodyInfo: {myBodyInfo}')
print(f'myBMI: {round(myBMI, 2)}')

