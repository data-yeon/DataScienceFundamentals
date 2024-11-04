
cityTempDict = {}

cityTempDict['서울'] = [-8, -4, 7, 13, 21, 29, 32, 33, 27, 19, 8, -5]
cityTempDict['춘천'] = [-14, -9, 3, 9, 19, 26, 31, 32, 24, 13, 2, -9]
cityTempDict['청주'] = [-5, -3, 9, 15, 23, 28, 30, 32, 29, 20, 12, -4]
cityTempDict['광주'] = [-5, -1, 8, 17, 23, 29, 32, 33, 25, 15, 6, -3]
cityTempDict['포항'] = [-4, 3, 12, 16, 24, 30, 33, 34, 28, 22, 11, -3]

print('cityTempDict:', cityTempDict)    # 딕셔너리 내용 확인

#######################################################################################
#
#   1. 도시 이름(cityName)과 월 별 평균 기온(monthlyTemp)을 비공개 속성으로 가지는
#   도시 기온(CityTemp) 클래스를 작성하시오.
#
#######################################################################################

class CityTemp():

    # 클래스 속성 정의
    # 초기화 메서드
    def __init__(self, cityName, monthlyTemp):
        self.cityName = cityName # 비공개 속성으로 도시이름 설정
        self.__monthlyTemp = monthlyTemp # 비공개 속성으로 월별 평균 기온 설정

    # 도시 이름을 가져오는 메서드
    def getCityName(self):
        return self.__cityName

    # 월별 평균 기온을 가져오는 메서드
    def getMonthlyTemp(self):
        return self.__monthlyTemp

print('cityTempDict:', cityTempDict)
#######################################################################################
#
#   2. 1에서 생성한 클래스에 도시의 이름과 월 별 평균 기온을 초기화하는 생성자 함수를 추가하시오.
#
#######################################################################################

class CityTemp():

    # 클래스 속성들

    def __init__(self, cityName, monthlyTemp):
        # 생성자 함수 정의
        # 비공개 속성 초기화
        self.__cityName = cityName
        self.__monthlyTemp = monthlyTemp

    # 도시 이름을 반환하는 메서드
    def getCityName(self):
        return self.__cityName

    # 월별 평균 기온을 반환하는 메서드
    def getMonthlyTemp(self):
        return self.__monthlyTemp

#######################################################################################
#
#   3. 도시 이름을 설정(변경)할 수 있는 setCityName() 클래스 함수,
#   도시의 이름을 얻을 수 있는 getCityName() 클래스 함수를 추가하시오.
#
#######################################################################################

class CityTemp:

    # 생성자 함수 정의
    def __init__(self, cityName, monthlyTemp):
        # 비공개 속성 초기화
        self.__cityName = cityName
        self.__monthlyTemp = monthlyTemp

    # 도시 이름을 설정하는 메서드
    def setCityName(self, cityName):
        self.__cityName = cityName

    # 도시 이름을 반환하는 메서드
    def getCityName(self):
        return self.__cityName

    # 월별 평균 기온을 반환하는 메서드
    def getMonthlyTemp(self):
        return self.__monthlyTemp

# 예시: 서울의 기온 데이터로 CityTemp 인스턴스 생성
seoul_temp = CityTemp("서울", cityTempDict["서울"])

# 도시 이름과 월별 기온 출력
print("도시 이름:", seoul_temp.getCityName())          # 도시 이름 출력
print("월별 평균 기온:", seoul_temp.getMonthlyTemp())  # 월별 기온 출력

# 도시 이름 변경
seoul_temp.setCityName("Seoul")
print("변경된 도시 이름:", seoul_temp.getCityName())