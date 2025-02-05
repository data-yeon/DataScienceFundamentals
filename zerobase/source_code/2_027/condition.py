exampleScore = int(input('시험 성적 입력 : '))
grades = ''

if exampleScore >= 90:
    grades = 'A'
elif exampleScore >= 80:
    grades = 'B'
elif exampleScore >= 70:
    grades = 'C'
elif exampleScore >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적: {} \t 학점: {}'.format(exampleScore, grades))


exampleScore = int(input('시험 성적 입력 : '))
grades = ''

if exampleScore >= 70:
    grades = 'C'
elif exampleScore >= 90:
    grades = 'A'
elif exampleScore >= 80:
    grades = 'B'
elif exampleScore >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적: {} \t 학점: {}'.format(exampleScore, grades))



exampleScore = int(input('시험 성적 입력 : '))
grades = ''

if exampleScore >= 70 and exampleScore < 80:
    grades = 'C'
elif exampleScore >= 90:
    grades = 'A'
elif exampleScore >= 80 and exampleScore < 90:
    grades = 'B'
elif exampleScore >= 60 and exampleScore < 70:
    grades = 'D'
else:
    grades = 'F'

print('성적: {} \t 학점: {}'.format(exampleScore, grades))



carDisplacement = int(input('자동차 배기량 입력 : '))

if carDisplacement < 1000:
    print('세금 : 100,000원')
elif carDisplacement < 2000 and carDisplacement >= 1000:
    print('세금 : 200,000원')
elif carDisplacement < 3000 and carDisplacement >= 2000:
    print('세금 : 300,000원')
elif carDisplacement < 4000 and carDisplacement >= 3000:
    print('세금 : 400,000원')
elif carDisplacement < 5000 and carDisplacement >= 4000:
    print('세금 : 500,000원')
elif carDisplacement >= 5000:
    print('세금 : 600,000원')