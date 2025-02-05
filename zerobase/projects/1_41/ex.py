# userMsg = input('메세지 입력: ')
# print('메세지 문자열 길이 : {}'.format(len(userMsg)))

# article = "귀도 반 로섬(네덜란드어: Guido van Rossum, 1956년 1월 31일 ~)은 네덜란드 출신의 소프트웨어 엔지니어이다. 프로그래밍 언어인 파이썬을 개발한 것으로 유명하며, 2018년 7월 12일 직에서 물러날 때까지 프로젝트의 자비로운 종신독재자를 맡았다."
#
# finded = article.find('귀도')
# print('객체지향 문자열 위치: {}'.format(finded))

width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))

triangleArea = width * height / 2
squareArea = height * height

print('-' *  25)
print('삼각형 넓이 : %.2f' % triangleArea)
print('사각형 넓이 : %.2f' % squareArea)
print('-' *  25)
