import random

visitors = []

for n in range(100):
    visitors.append(random.randint(1, 100))

group1, group2, group3, group4, group5 = 0,0,0,0,0
for age in visitors:

    if age >= 0 and age <= 7:
        group1 += 1
    elif age >= 8 and age <= 13:
        group2 += 1
    elif age >= 14 and age <= 19:
        group3 += 1
    elif age >= 20 and age <= 64:
        group4 += 1
    else:
        group5 += 1

group1Price = group1 * 0
group2Price = group2 * 200
group3Price = group3 * 300
group4Price = group4 * 500
group5Price = group5 * 0

print('-' * 25)
print(f'영유아\t: {group1}명\t: {group1Price}원')
print(f'어린이\t: {group2}명\t: {group2Price}원')
print(f'청소년\t: {group3}명\t: {group3Price}원')
print(f'성인\t\t: {group4}명\t: {group4Price}원')
print(f'어르신\t: {group5}명\t: {group5Price}원')

sum = group1Price + group2Price + group3Price + group4Price + group5Price
sumFormat = format(sum, ',')
print('-' * 25)
print(f'1일 요금 총합계: {sumFormat}원')
print('-' * 25)

