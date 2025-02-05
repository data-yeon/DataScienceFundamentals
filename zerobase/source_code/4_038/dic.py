# memInfo = {'이름':'홍길동', '메일':'gildong@gmail.com', '학년':3, '취미':['농구', '게임']}
#
# print('이름' in memInfo)
# print('메일' in memInfo)
# print('학년' in memInfo)
# print('취미' in memInfo)
#
# print('name' not in memInfo)
# print('mail' not in memInfo)
# print('grade' not in memInfo)
# print('hobby' not in memInfo)

# print('홍길동' in memInfo)
# print('gildong@gmail.com' in memInfo)
# print(3 in memInfo)
# print(['농구', '게임'] in memInfo)


# print('len(memInfo) : {}'.format(len(memInfo)))
#
# print('memInfo: {}'.format(memInfo))
#
# memInfo.clear()
# print('memInfo: {}'.format(memInfo))




myInfo = {'이름':'Hong Gildong',
          '나이':'30',
          '연락처': '010-1234-5678',
          '주민등록번호':'840315-1234567',
          '주소':'대한민국 서울'}
print('myInfo: {}'.format(myInfo))

deleteItems = ['연락처', '주민등록번호']

for item in deleteItems:
    if (item in myInfo):
        del myInfo[item]

print('myInfo: {}'.format(myInfo))



