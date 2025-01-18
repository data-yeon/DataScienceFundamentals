# 최대 공약수를 구해서 최소 공배수를 구하기
num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

maxNum = 0

for i in range(1, (num1 + 1)):
    if num1 % i == 0 and num2 % i == 0:
        print("공약수 : {}".format(i))
        maxNum = i

print("최대 공약수 : {}".format(maxNum))


minNum =  (num1 * num2 )// maxNum
print ("최소 공배수 :{}".format(minNum))