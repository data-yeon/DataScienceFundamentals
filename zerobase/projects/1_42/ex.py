

pi = 3.14
radius = float(input("반지름 (cm)입력 : "))

circleArea = pi * radius * radius
circleLength = 2 * pi * radius

print('원의 넓이\t: %d' % circleArea)
print('원의 둘레 길이\t: %d' % circleLength)

print('원의 넓이\t: %.1f' % circleArea)
print('원의 둘레 길이\t: %.1f' % circleLength)

print('원의 넓이\t: %.3f' % circleArea)
print('원의 둘레 길이\t: %.3f' % circleLength)