students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students: {}'.format(students))

students.reverse()
print('students: {}'.format(students))



numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print('numbers: {}'.format(numbers))

numbers.reverse()
print('numbers: {}'.format(numbers))





secret = '27156231'
secretList = []
solvedList = ''

for cha in secret:
    secretList.append(int(cha))

secretList.reverse()
print(secretList)

val = secretList[0] * secretList[1]
secretList.insert(2, val)
print(secretList)

val = secretList[3] * secretList[4]
secretList.insert(5, val)
print(secretList)

val = secretList[6] * secretList[7]
secretList.insert(8, val)
print(secretList)

val = secretList[9] * secretList[10]
secretList.insert(11, val)
print(secretList)



