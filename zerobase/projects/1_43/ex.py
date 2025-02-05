# BMI = 몸무게(kg) / ( 신장 (m) * 신장 (m))


weight = input('체중 입력 (g) : ')
height = input('신장 입력 (cm) : ')

if weight.isdigit():
    weight = int(weight) / 1000 # 문자열로 받은걸 변환

if height.isdigit():
    height = int(height) / 100

print('체중 : {}'.format(weight))
print('신장 : {}'.format(height))
bmi =weight/(height * height)

print('BMI :  %.2f' % bmi)