
selectNum = int(input("출퇴근 대상자 인가요? 1.네 \t 2.아니요 : "))

if selectNum == 1:
    print('교통수단을 선택하세요. ')
    trans = int(input("1. 도보, 자전거 \t 2. 버스, 지하철 \t 3. 자가용 : "))
    print("-"*25)
    if trans == 1:
        print("세금 감면 5%")
    elif trans == 2:
        print("세금 감면 3%")
    elif trans == 3:
        print("추가 세금 1%")
elif selectNum == 2:
    print("세금 변동 없음")
    print("-" * 25)
else :
    print("잘못 입력하셨습니다.")