# try:
#     inputData = input('input number: ')
#     numInt = int(inputData)
#
# except:
#     print('exception raise!!')
#     print('not number!!')
#     numInt = 0
#
# else:
#     if numInt % 2 == 0:
#         print('inputData is even number!!')
#     else:
#         print('inputData is odd number!!')
#
# finally:
#     print(f'inputData: {inputData}')




eveList = []; oddList = []; floatList = []
dataList = []

n = 1
while n < 6:

    try:
        data = input('input number: ')
        floatNum = float(data)

    except:
        print('exception raise!!')
        print('input number again!!')
        continue

    else:

        if floatNum - int(floatNum) != 0:
            print('float number!')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('even number!')
                eveList.append(int(floatNum))

            else:
                print('odd number')
                oddList.append(int(floatNum))

        n += 1

    finally:
        dataList.append(data)


print(f'eveList: {eveList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')
print(f'dataList: {dataList}')
