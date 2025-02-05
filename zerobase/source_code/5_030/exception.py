nums = []
n = 1
while n < 6:

    try:
        num = int(input('input number: '))

    except:
        print('예외 발생')
        continue

    else:
        if num % 2 == 0:
            nums.append(num)
            n += 1

        else:
            print('입력한 숫자는 홀수 입니다.', end='')
            print('다시 입력 하세요.')
            continue


print(f'nums: {nums}')



eveList = []; oddList = []; floatList = []

n = 1
while n < 6:

    try:
        num = float(input('input number: '))

    except:
        print('exception raise!!')
        print('input number again!!')
        continue

    else:

        if num - int(num) != 0:
            print('float number!')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('even number!')
                eveList.append(int(num))

            else:
                print('odd number')
                oddList.append(int(num))

        n += 1

print(f'eveList: {eveList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')

    
