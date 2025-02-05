# def calculator(n1, n2):
#     return n1 + n2
#
# returnValue = calculator(10, 20)
# print(f'returnValue: {returnValue}')
#
#
#
# calculator = lambda n1, n2: n1 + n2
# returnValue = calculator(10, 20)
# print(f'returnValue: {returnValue}')


getTriangleArea = lambda n1, n2: n1 * n2 / 2
getSquareArea = lambda n1, n2: n1 * n2
getSircleArea = lambda r: radius * radius * 3.14

width = int(input('가로 길이 입력: '))
height = int(input('세로 길이 입력: '))
radius = int(input('반지름 길이 입력: '))

triangleValue = getTriangleArea(width, height)
squareValue = getSquareArea(width, height)
radiusValue = getSircleArea(radius)

print(f'삼각형 넓이: {triangleValue}')
print(f'사각형 넓이: {squareValue}')
print(f'원 넓이: {radiusValue}')



