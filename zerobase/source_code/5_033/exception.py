class NotUseZeroException(Exception):

    def __init__(self, n):
        super().__init__(f'{n}은 사용할 수 없습니다!!')


def divCalculator(num1, num2):

    if num2 == 0:
        raise NotUseZeroException(num2)
    else:
        print(f'{num1} / {num2} = {num1 / num2}')

num1 = int(input('input number1: '))
num2 = int(input('input number2: '))

try:
    divCalculator(num1, num2)
except NotUseZeroException as e:
    print(e)



class PasswordLengthShortException(Exception):

    def __init__(self, str):
            super().__init__(f'{str}: 길이 5미만!!')

class PasswordLengthLongException(Exception):

    def __init__(self, str):
            super().__init__(f'{str}: 길이 10초과!!')

class PasswordWrongException(Exception):

    def __init__(self, str):
            super().__init__(f'{str} 잘못된 비밀번호!!')



adminPw = input('input admin password: ')

try:
    if len(adminPw) < 5:
        raise PasswordLengthShortException(adminPw)

    elif len(adminPw) > 10:
        raise PasswordLengthLongException(adminPw)

    elif adminPw != 'admin1234':
        raise PasswordWrongException(adminPw)

    elif adminPw == 'admin1234':
        print('빙고!')

except PasswordLengthShortException as e1:
    print(e1)

except PasswordLengthLongException as e2:
    print(e2)

except PasswordWrongException as e3:
    print(e3)


