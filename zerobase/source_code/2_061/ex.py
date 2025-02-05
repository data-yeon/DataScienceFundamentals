'''
윤년 구하기
연도가 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년이다.
또는
연도가 400으로 나누어 떨어지면 윤년이다.
'''

year = int(input('연도 입력: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('{}년: 윤년!!'.format(year))
else:
    print('{}년: 평년'.format(year))
    
    

for year in range(2021, (2021+101)):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('{}년: 윤년!!'.format(year))
    else:
        print('{}년: 평년'.format(year))