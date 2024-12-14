#######################################################################################
#
#   3. 도시 이름을 설정(변경)할 수 있는 setCityName() 클래스 함수,
#   도시의 이름을 얻을 수 있는 getCityName() 클래스 함수를 추가하시오.
#
#######################################################################################

class CityTemp():

    # 클래스 속성들
    cityName = None
    monthlyTemp = None

    def __init__(self, cityName, monthlyTemp):
        # 생성자 함수 정의
        self.cityName = cityName
        self.monthlyTemp = monthlyTemp

    # 클래스 함수들 - 도시 이름 설정, 가져오기

    def setCityName(self, cityName):
        self.cityName = cityName

    # 도시이름을 반환하는 메서드
    def getCityName(self):
        return self.cityName