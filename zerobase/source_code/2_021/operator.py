import random

import operator

num1 = 8
num2 = 3
print('{} + {} : {}'.format(num1, num2, operator.add(num1, num2)))
print('{} - {} : {}'.format(num1, num2, operator.sub(num1, num2)))
print('{} * {} : {}'.format(num1, num2, operator.mul(num1, num2)))
print('{} / {} : {}'.format(num1, num2, operator.truediv(num1, num2)))
print('{} % {} : {}'.format(num1, num2, operator.mod(num1, num2)))
print('{} // {} : {}'.format(num1, num2, operator.floordiv(num1, num2)))
print('{} ** {} : {}'.format(num1, num2, operator.pow(num1, num2)))

num1 = 8
num2 = 3
print('{} == {} : {}'.format(num1, num2, operator.eq(num1, num2)))
print('{} != {} : {}'.format(num1, num2, operator.ne(num1, num2)))
print('{} > {} : {}'.format(num1, num2, operator.gt(num1, num2)))
print('{} >= {} : {}'.format(num1, num2, operator.ge(num1, num2)))
print('{} < {} : {}'.format(num1, num2, operator.lt(num1, num2)))
print('{} <= {} : {}'.format(num1, num2, operator.le(num1, num2)))

flag1 = True
flag2 = False
print('{} and {} : {}'.format(flag1, flag2, operator.and_(flag1, flag2)))
print('{} or {} : {}'.format(flag1, flag2, operator.or_(flag1, flag2)))
print('not {} : {}'.format(flag1, operator.not_(flag1)))

# age = int(input('나이 입력 : '))
# vaccine = (age < 20) or (age >= 65)
# print('age: {}, result: {}'.format(age, vaccine))

age = int(input('나이 입력 : '))
vaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
print('age: {}, result: {}'.format(age, vaccine))

import random

rInt = random.randint(10, 100)

num10 = operator.floordiv(rInt, 10)
num1 = operator.mod(rInt, 10)

print('난수 : {}'.format(rInt))
print('십의 자리 : {}'.format(num10))
print('일의 자리 : {}'.format(num1))

print('십의 자리는 3의 배수이다. : {}'.format(operator.mod(num10, 3) == 0))
print('일의 자리는 3의 배수이다. : {}'.format(operator.mod(num1, 3) == 0))