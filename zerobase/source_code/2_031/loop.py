for i in range(1, 11, 1):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, 10, 1):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(11):
    print(i)

startNum = int(input('반복의 시작 입력 : '))
endNum = int(input('반복의 끝 입력 : '))

for i in range(startNum, (endNum+1)):
    print(i)

for i in range(startNum, (endNum+1), 2):
    print(i)

for i in range(1, 101):
    if i % 3 == 0:
        print(i)
