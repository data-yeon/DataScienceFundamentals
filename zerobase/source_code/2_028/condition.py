exampleScore = int(input('점수 입력 : '))

if exampleScore < 60:
    print('재시험 대상입니다.')

else:
    if exampleScore >= 90:
        print('A')
    elif exampleScore >= 80:
        print('B')
    elif exampleScore >= 70:
        print('C')
    elif exampleScore >= 60:
        print('D')



selectNum = int(input('출퇴근 대상자 인가요? 1.Yes \t 2.No'))

if selectNum == 1:
    print('교통수단을 선택하세요.')
    trans = int(input('1.도보,자전거 \t 2.버스,지하철 \t 3.자가용'))

    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('추가 세금 1%')

elif selectNum == 2:
    print('세금 변동 없습니다.')
else:
    print('잘못 입력했습니다.')


inputAge = int(input('나이 입력 : '))

if inputAge <= 19 or inputAge >= 65:
    endNum = int(input('출생 연도 끝자리 입력 : '))
    if endNum == 1 or endNum == 6:
        print('월요일 접종 가능!')
    elif endNum == 2 or endNum == 7:
        print('화요일 접종 가능!')
    elif endNum == 3 or endNum == 8:
        print('수요일 접종 가능!')
    elif endNum == 4 or endNum == 9:
        print('목요일 접종 가능!')
    elif endNum == 5 or endNum == 0:
        print('금요일 접종 가능!')
else:
    print('하반기 일정 확인하세요.')

