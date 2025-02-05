studentTuple1 = ('홍길동', '박찬호', '이용규')
studentTuple2 = ('박승철', '김지은', '강호동')

studentTuple3 = studentTuple1 + studentTuple2
print('studentTuple3: {}'.format(studentTuple3))


studentList1 = ['홍길동', '박찬호', '이용규']
studentList2 = ['박승철', '김지은', '강호동']

studentList1.extend(studentList2)
print('studentList1: {}'.format(studentList1))


studentTuple1 = ('홍길동', '박찬호', '이용규')
studentTuple2 = ('박승철', '김지은', '강호동')

studentTuple1.extend(studentTuple2)
print('studentTuple1: {}'.format(studentTuple1))




myFavoriteNumbers = (1, 3, 5, 6, 7)
friendFavoriteNumbers = (2, 3, 5, 8, 10)

print('myFavoriteNumbers: {}'.format(myFavoriteNumbers))
print('friendFavoriteNumbers: {}'.format(friendFavoriteNumbers))

for number in friendFavoriteNumbers:
    if number not in myFavoriteNumbers:
        myFavoriteNumbers = myFavoriteNumbers + (number, )

print('myFavoriteNumbers: {}'.format(myFavoriteNumbers))