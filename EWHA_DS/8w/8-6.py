#######################################################################################
#
#   5. 도시의 월 별 기온을 설정(변경)할 수 있는 setCityTemp() 클래스 함수,
#   도시의 월 별 기온을 얻을 수 있는 getCityTemp() 클래스 함수를 추가하시오.
#

#######################################################################################

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
    def __init__(self, cityName, monthlyTemp):
        self.__cityName = cityName #  도시이름 비공개 속성
        self.__monthlyTemp = monthlyTemp # 월 별 평균 기온
    def getCityName(self):
        return self.__cityName
    def getMonthlyTemp(self):
        return sum(self.__monthlyTemp)/ len(self.__monthlyTemp)


# print('cityTempDict:', cityTempDict)
# 도시별 인스턴스 생성 및 저장
city_instances = []
for city, temps in cityTempDict.items():
    city_instance = CityTemp(city, temps)
    city_instances.append(city_instance)



#######################################################################################
#
#   6. 클래스의 월 평균 기온 속성 값을 이용해서 연 평균 기온을 계산하는 calcYearAvgTemp() 클래스 함수를 작성하시오.
#
#######################################################################################

class CityTemp():

    # 클래스 속성들

    def __init__(self, cityName, monthlyTemp):
        # 생성자 함수 정의
        self.__cityName = cityName
        self.__monthlyTemp = monthlyTemp



    # 클래스 함수들 - 도시 이름 설정, 가져오기
    def setCityName(self, cityName):
        self.__cityName = cityName

    # 도시 이름 반환 메서드
    def getCityName(self):
        return self.__cityName
    # 클래스 함수들 - 도시 온도 설정, 가져오기
    # 월별 기온 설정 메서드
    def setMonthlyTemp(self, monthlyTemp):
        self.__monthlyTemp = monthlyTemp

    # 월별 기온 반환 메서드
    def getMonthlyTemp(self):
        return self.__monthlyTemp

    # 클래스 함수들 - 도시 온도 합(sum) 계산, 도시 온도 평균(avg) 계산
    # 도시의 월별 기온 합계 계산 메서드
    def sumMonthlyTemp(self):
        return sum(self.__monthlyTemp)
    # 도시의 월별 기온 평균 메서드
    def calcYearAvgTemp(self):
        return sum(self.__monthlyTemp) / len(self.__monthlyTemp)
