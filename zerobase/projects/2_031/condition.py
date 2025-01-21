exampleScore = int(input("시험 점수 입력 : "))

if exampleScore < 60 :
    print('재시험 대상입니다.')
else :
    if exampleScore >= 90:
        print('A')
    elif exampleScore >= 80:
        print('B')
    elif exampleScore >= 70:
        print('C')
    elif exampleScore >= 60:
        print('D')