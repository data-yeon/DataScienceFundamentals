
import datetime

today = datetime.datetime.today()

myAge = input("나이 입력: ")

if myAge.isdigit():
    afterAge = 100 - int(myAge)
    myHundred = today.year + afterAge
    
    print('내가 100살이 되는 해는 {}년({}년후)이다.'.format(myHundred, afterAge))
    pass
else:
    print("잘못 입력하셨습니다.")