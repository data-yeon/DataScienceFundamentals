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
#   4. 포항의 월 평균 기온을 데이터로 가지는 클래스 인스턴스를 생성하시오.
#   그리고 생성한 인스턴스에서 도시 이름을 출력하시오.
#
#######################################################################################

ct = getMonthlyTemp('포항')
