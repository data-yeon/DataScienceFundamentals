subject = ['국어', '영어', '수학', '과학', '국사']
scores = {}

for s in subject:
    score = input(s + ' 점수 입력: ')
    scores[s] = score

print(f'과목별 점수 : {scores}')




members = {'urkpo':'0928^7$',
           'xxayv':'%2*9$91',
           'lsqvx':'!0%)&&4',
           'heums':'%@3^0%3',
           'uwcmc':'85236(&',
           'iemwv':')8!36^&',
           'sqblx':')^2)9!(',
           'jbbpy':'67269*3',
           'hjkwu':'$&@@#64',
           'fvwwy':'82$%)31'}

memID = input('ID 입력: ')
memPW = input('PW 입력: ')

if memID in members:
    if members[memID] == memPW:
        print('로그인 성공!!')
    else:
        print('비밀번호 확인!!')
else:
    print('아이디 확인!!')



