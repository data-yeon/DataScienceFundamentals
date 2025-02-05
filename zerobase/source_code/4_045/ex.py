# tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
# tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)
#
# tempHap = list(tuple1)
# tempGyo = list()
#
# for n in tuple2:
#     if n not in tempHap:
#         tempHap.append(n)
#     else:
#         tempGyo.append(n)
#
# tempHap = tuple(sorted(tempHap))
# tempGyo = tuple(sorted(tempGyo))
#
# print(f'합집합(중복X)\t : {tempHap}')
# print(f'교집합\t\t : {tempGyo}')


tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

tempHap = tuple1 + tuple2
print(f'tempHap : {tempHap}')
tempGyo = list()

tempHap = list(tempHap)
print(f'tempHap : {tempHap}')

for n in tempHap:
    if tempHap.count(n) > 1:
        tempGyo.append(n)
        tempHap.remove(n)

print(f'tempHap : {tempHap}')
print(f'합집합(중복X): {tuple(sorted(tempHap))}')

print(f'tempGyo : {tempGyo}')
print(f'교집합 : {tuple(sorted(tempGyo))}')