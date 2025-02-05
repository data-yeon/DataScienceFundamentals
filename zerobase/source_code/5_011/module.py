import calculator

calculator.add(10, 20)
calculator.sub(10, 20)
calculator.mul(10, 20)
calculator.div(10, 20)



import calculator as cal

cal.add(10, 20)
cal.sub(10, 20)
cal.mul(10, 20)
cal.div(10, 20)

#calculator.div(10, 20)



from calculator import add
from calculator import sub

# from calculator import add, sub
# from calculator import *

add(10, 20)
sub(10, 20)

# mul(10, 20)


import scores as sc

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

sc.addScore(korScore)
sc.addScore(engScore)
sc.addScore(matScore)

print(sc.getScores())
print(sc.getTotalScore())
print(sc.getAvgScore())




