# num1 = int(input('input numer1: '))
# num2 = int(input('input numer2: '))
#
# try:
#     print(f'num1 / num2 = {num1 / num2}')
# except:
#     print('0으로 나눌 수 없습니다.')
#
# print(f'num1 * num2 = {num1 * num2}')
# print(f'num1 - num2 = {num1 - num2}')
# print(f'num1 + num2 = {num1 + num2}')
#
#
#
#
# num1 = int(input('input numer1: '))
# num2 = int(input('input numer2: '))
#
# try:
#     print(f'num1 / num2 = {num1 / num2}')
# except Exception as e:
#     print(f'exception: {e}')
#
# print(f'num1 * num2 = {num1 * num2}')
# print(f'num1 - num2 = {num1 - num2}')
# print(f'num1 + num2 = {num1 + num2}')




# try:
#     num1 = int(input('input numer1: '))
#     num2 = int(input('input numer2: '))
# except Exception as e:
#     print(f'exception: {e}')
#     num1 = 10
#     num2 = 20
#
# try:
#     print(f'num1 / num2 = {num1 / num2}')
# except ZeroDivisionError as e:
#     print(f'exception: {e}')
#
# print(f'num1 * num2 = {num1 * num2}')
# print(f'num1 - num2 = {num1 - num2}')
# print(f'num1 + num2 = {num1 + num2}')





# def divCalculator(n1, n2):
#
#     if n2 != 0:
#         print(f'{n1} / {n2} = {n1 / n2}')
#     else:
#         raise Exception('0으로 나눌 수 없습니다.')
#
#
# num1 = int(input('input numer1: '))
# num2 = int(input('input numer2: '))
# divCalculator(num1, num2)



# def divCalculator(n1, n2):
#
#     if n2 != 0:
#         print(f'{n1} / {n2} = {n1 / n2}')
#     else:
#         raise Exception('0으로 나눌 수 없습니다.')
#
#
# num1 = int(input('input numer1: '))
# num2 = int(input('input numer2: '))
#
# try:
#     divCalculator(num1, num2)
# except Exception as e:
#     print(f'Exception: {e}')



def sendSMS(msg):

    if len(msg) > 10:
        raise Exception('길이 초과!! MMS전환 후 발송!!', 1)

    else:
        print('SMS 발송!!')

def sendMMS(msg):

    if len(msg) <= 10:
        raise Exception('길이 미달!! SMS전환 후 발송!!', 2)
    else:
        print('MMS 발송!!')


msg = input('input message: ')

try:
    sendSMS(msg)

except Exception as e:
    print(f'e: {e.args[0]}')
    print(f'e: {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)



