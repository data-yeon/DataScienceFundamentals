members = {}

n = 1
while n < 3:
    mail = input('메일 입력: ')
    pw = input('비번 입력: ')

    if mail in members:
        print('이미 사용 중인 메일 계정입니다.')
        continue
    else:
        members[mail] = pw
        n+= 1

for key in members.keys():
    print(f'{key} : {members[key]}')


#회원 삭제
while True:
    delMail = input('삭제할 계정 입력: ')

    if delMail in members:
        delPw = input('비번 입력: ')
        if members[delMail] == delPw:
            del members[delMail]
            print(f'{delMail}님 삭제 완료!')
            break
        else:
            print('비번 확인 요망!')
    else:
        print('계정 확인 요망!')


for key in members.keys():
    print(f'{key} : {members[key]}')

