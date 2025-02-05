# n1= 10; n2 = 0
#
# print(n1 / n2)
# print(n1 * n2)
# print(n1 - n2)
# print(n1 + n2)



# n1= 10; n2 = 0
#
# try:
#     print(n1 / n2)
# except:
#     print('예상치 못한 예외가 발생했습니다.')
#     print('다른 프로그램 실행에는 문제 없습니다.')
#
# print(n1 * n2)
# print(n1 - n2)
# print(n1 + n2)

nums = []

n = 1
while n < 6:
    try:
        num = int(input('input number: '))
    except:
        print('예외 발생!')
        continue

    nums.append(num)
    n += 1

print(f'nums: {nums}')




