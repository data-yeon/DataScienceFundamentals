inputAge = int(input('나의 입력: '))

if inputAge <= 19 or inputAge >= 65:
    endNum = int(input('출생 연도 끝자리 입력: '))
    if endNum == 1 or endNum == 6:
        print('월요일 접종 가능!!')
    elif endNum == 2 or endNum == 7:
        print('화요일 접종 가능!!')
    elif endNum == 3 or endNum == 8:
        print('수요일 접종 가능!!')
    elif endNum == 4 or endNum == 9:
        print('목요일 접종 가능!!')
    elif endNum == 5 or endNum == 0:
        print('금요일 접종 가능!!')
else:
    print('하반기 일정 확인하세요.')




byInch = 0.039
lengthMM = int(input('길이(mm) 입력: '))
lengthInch = lengthMM * byInch

print('{}mm -> {}inch'.format(lengthMM, lengthInch))


