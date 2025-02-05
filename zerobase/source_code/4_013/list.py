students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))

students.remove('강호동')
print('students : {}'.format(students))
print('students의 길이 : {}'.format(len(students)))


students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은', '강호동']
print(students)

while '강호동' in students:
    students.remove('강호동')

print(students)


myList = ['마케팅 회의', '회의록 정리', '점심 약속', '월간 업무 보고', '치과 방문', '마트 장보기']
print('일정 : {}'.format(myList))

removeItem = input('삭제 대상 입력: ')
myList.remove(removeItem)
print('일정 : {}'.format(myList))


subjects = ['국어', '영어', '수학', '과학', '국사']
print('시험 과목표 : {}'.format(subjects))

removeSubject = input('삭제 과목명 입력: ')
while removeSubject in subjects:
    subjects.remove(removeSubject)

print('시험 과목표 : {}'.format(subjects))



