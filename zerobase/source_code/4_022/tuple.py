studentsTuple = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

searchName = input('학생 이름 입력: ')
if searchName in studentsTuple:
    print('{} 학생은 우리반 학생입니다.'.format(searchName))
else:
    print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))



studentsList = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

searchName = input('학생 이름 입력: ')
if searchName in studentsList:
    print('{} 학생은 우리반 학생입니다.'.format(searchName))
else:
    print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))



pythonStr = '파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, ' \
            '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. ' \
            '파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'

print('{} : {}'.format('Python', 'Python' in pythonStr))        # True
print('{} : {}'.format('python', 'python' in pythonStr))        # False

print('{} : {}'.format('파이썬', '파이썬' in pythonStr))          # True
print('{} : {}'.format('파이선', '파이선' in pythonStr))          # False

print('{} : {}'.format('귀도', '귀도' in pythonStr))              # True
print('{} : {}'.format('객체지향적', '객체지향적' in pythonStr))    # True




import random

randomNumbers = random.sample(range(1, 11), 5)

userNumber = int(input('숫자 입력(확율 50%): '))
if userNumber in randomNumbers:
    print('빙고!')
else:
    print('다음 기회에~')

print('randomNumbers: {}'.format(randomNumbers))
print('userNumber: {}'.format(userNumber))



wrongWord = ['쩔었다', '짭새', '꼽사리', '먹튀', '지린', '쪼개다', '뒷담 까다']
sentence = '짭새 등장에 강도들은 모두 쩔었다. 그리고 강도 들은 지린 듯 도망갔다.'

for word in wrongWord:
    if word in sentence:
        print('비속어: {}'.format(word))