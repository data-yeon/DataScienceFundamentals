# 유클리드 호제법
num1 = int(input("1보다 큰 정수 입력: "))
num2 = int(input("1보다 큰 정수 입력: "))

temp1 = num1
temp2 = num2

while temp2 > 0 :
    temp = temp2
    temp2 =  temp1 % temp2
    temp1 = temp  # 이런식으로 해서 temp2가 0보다 클 때 까지 .

print('{}, {} 의 최대공약수 : {}'.format(num1, num2, temp1))