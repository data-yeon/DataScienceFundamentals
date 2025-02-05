userName = '홍길동'
print(userName)

userAge = 20
print(userAge)


print('User name : ', userName)
print('User age : ', userAge)
print('User name : ', userName, ', User age : ', userAge)

print(f'User name : {userName}')
print(f'User age : {userAge}')
print(f'User name : {userName}, User age : {userAge}')

print(f'User name\t:\t{userName}\nUser age\t:\t{userAge}')

width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))

triangle = width * height / 2
square = width * height

print('width : ', width)
print('height : ', height)

print('Triangle : ', triangle)
print('Square : ', square)

print(f'width : {width}, height : {height}')
print(f'Triangle : {triangle}, Square : {square}')

print(f'width : {width},\t\theight : {height}')
print(f'Triangle : {triangle},\tSquare : {square}')