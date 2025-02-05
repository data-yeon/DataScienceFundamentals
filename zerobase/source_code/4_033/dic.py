students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}

print('students[\'s1\']:{}'.format(students['s1']))
print('students[\'s2\']:{}'.format(students['s2']))
print('students[\'s3\']:{}'.format(students['s3']))
print('students[\'s4\']:{}'.format(students['s4']))
print('students[\'s5\']:{}'.format(students['s5']))


memInfo = {'이름':'홍길동', '취미':['농구', '게임', '여행']}
print('memInfo[\'이름\']:{}'.format(memInfo['이름']))
print('memInfo[\'취미\']:{}'.format(memInfo['취미']))
print('memInfo[\'취미[0]\']:{}'.format(memInfo['취미'][0]))
print('memInfo[\'취미[1]\']:{}'.format(memInfo['취미'][1]))
print('memInfo[\'취미[2]\']:{}'.format(memInfo['취미'][2]))

for h in memInfo['취미']:
    print(h)

for i, h in enumerate(memInfo['취미']):
    print('index:{} --> {}'.format(i, h))



students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}
print('students[\'s6\']:{}'.format(students['s6']))



students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':'박승철', 's5':'김지은'}
print('students.get(\'s5\'):{}'.format(students.get('s5')))
print('students.get(\'s6\'):{}'.format(students.get('s6')))


myInfo = {'이름':'박경진',
          '전공':'computer',
          '메일':'jin@naver.com',
          '학년':3,
          '주소':'대한민국 서울',
          '취미':['요리', '여행']}

print('myInfo[\'이름\']: {}'.format(myInfo['이름']))
print('myInfo[\'전공\']: {}'.format(myInfo['전공']))
print('myInfo[\'메일\']: {}'.format(myInfo['메일']))
print('myInfo[\'학년\']: {}'.format(myInfo['학년']))
print('myInfo[\'주소\']: {}'.format(myInfo['주소']))
print('myInfo[\'취미\']: {}'.format(myInfo['취미']))

print('myInfo.get(\'이름\'): {}'.format(myInfo.get('이름')))
print('myInfo.get(\'전공\'): {}'.format(myInfo.get('전공')))
print('myInfo.get(\'메일\'): {}'.format(myInfo.get('메일')))
print('myInfo.get(\'학년\'): {}'.format(myInfo.get('학년')))
print('myInfo.get(\'주소\'): {}'.format(myInfo.get('주소')))
print('myInfo.get(\'취미\'): {}'.format(myInfo.get('취미')))



print(f'myInfo.get(\'취미\'): {myInfo.get("취미")}')

