# 수 두개의 공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
#
# common = []
# for i in range(1, (num1 + 1)):
#     if num1 % i == 0 and num2 % i == 0:
#         common.append(i)
#
# if len(common) > 0:
#     try:
#         with open('C:/pythonTxt/common.txt', 'a') as f:
#             f.write(f'{num1}와 {num2}의 공약수: ')
#             f.write(f'{common}\n')
#
#     except Exception as e:
#         print(e)
#
#     else:
#         print('common factor write complete!')


# 수 두개의 최대공약수
num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
maxComNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        maxNum = i

try:
    with open('C:/pythonTxt/maxComNum.txt', 'a') as f:
        f.write(f'{num1}와 {num2}의 최대공약수: {maxNum}\n')

except Exception as e:
    print(e)

else:
    print('max common factor write complete!')



# 수 세개의 공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
# num3 = int(input('1보다 큰 정수 입력: '))
#
# common = []
# for i in range(1, (num1 + 1)):
#     if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
#         common.append(i)
#
# if len(common) > 0:
#     try:
#         with open('C:/pythonTxt/common.txt', 'a') as f:
#             f.write(f'{num1}, {num2}, {num3}의 공약수: ')
#             f.write(f'{common}\n')
#
#     except Exception as e:
#         print(e)
#
#     else:
#         print('common factor write complete!')

# 수 세개의 최대공약수
# num1 = int(input('1보다 큰 정수 입력: '))
# num2 = int(input('1보다 큰 정수 입력: '))
# num3 = int(input('1보다 큰 정수 입력: '))
# maxComNum = 0
#
# for i in range(1, (num1 + 1)):
#     if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
#         maxComNum = i
#
# try:
#     with open('C:/pythonTxt/maxComNum.txt', 'a') as f:
#         f.write(f'{num1}, {num2}, {num3}의 최대공약수: {maxComNum}\n')
#
# except Exception as e:
#     print(e)
#
# else:
#     print('max common factor write complete!')