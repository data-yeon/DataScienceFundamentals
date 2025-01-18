
min_temp = int(input("최저 기온 입력: "))
max_temp = int(input("최고 기온 입력: "))


# 일교차가 11도 이상인 경우 출력 내용
# 일교차 영어:
diurnal_temp= max_temp -min_temp

if diurnal_temp >= 11:
    print(f"일교차 :{diurnal_temp} 도")
    print("감기 조심하세요.")
else :
    print(f"일교차 :{diurnal_temp} 도")
    print("산책하기 좋은 날씨 입니다.")