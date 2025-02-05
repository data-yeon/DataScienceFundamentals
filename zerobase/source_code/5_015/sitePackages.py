import sys

for path in sys.path:
    print(path)


from calculator import cal

print(f'cal.add(10, 20): {cal.add(10, 20)}')
print(f'cal.sub(10, 20): {cal.sub(10, 20)}')
print(f'cal.mul(10, 20): {cal.mul(10, 20)}')
print(f'cal.div(10, 20): {cal.div(10, 20)}')



from divisor_pac import divisor_mod as dm

print(f'10의 약수: {dm.divisor(10)}')
print(f'50까지의 소수: {dm.prime_number(50)}')





