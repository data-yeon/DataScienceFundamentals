userName = '홍길동'
print(userName)

userAge = 20
print(userAge)


print('User name : {}'.format(userName))
print('User age : {}'.format(userAge))
print('User name : {}, User age : {}'.format(userName, userAge))

print('나의 이름은 {}이고, 나이는 {}살 입니다. {} 이름은 아버님께서 지어 주셨습니다.'.format(userName, userAge, userName))

print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0} 이름은 아버님께서 지어 주셨습니다.'.format(userName, userAge))


print('User name : %s' % userName)
print('User age : %d' % userAge)
print('User name : %s, User age : %d' % (userName, userAge))

print('Pi : %f' % 3.14)
print('Pi : %d' % 3.14)

print('Pi : %.0f' % 3.141592)
print('Pi : %.2f' % 3.141592)
print('Pi : %.4f' % 3.141592)
print('Pi : %.6f' % 3.141592)

radius = float(input('반지름 입력 : '))
pi = float(input('원주율 입력 : '))

print('radius : {}'.format(radius))
print('pi : {}'.format(pi))
print('radius : {}, pi : {}'.format(radius, pi))
print('radius : %f, pi : %f' % (radius, pi))
print('radius : %.2f, pi : %.2f' % (radius, pi))

circleArea = radius * radius * pi
circleLengh = 2 * pi * radius
