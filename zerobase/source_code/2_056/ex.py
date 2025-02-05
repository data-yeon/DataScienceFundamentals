for i in range(1, 101):
    if i <= 9:
        if i % 2 == 0:
            print('[{}]: 짝수!'.format(i))
        else:
            print('[{}]: 홀수!'.format(i))
    else:
        num10 = i // 10
        num1 = i % 10

        result10 = ''
        if num10 % 2 == 0:
            result10 = '짝수!!'
        else:
            result10 = '홀수!!'

        result1 = '0'
        if num1 != 0:
            if num1 % 2 == 0:
                result1 = '짝수!!'
            else:
                result1 = '홀수!!'

        print('[{}] 십의자리: {}, 일의자리: {}'.format(i, result10, result1))