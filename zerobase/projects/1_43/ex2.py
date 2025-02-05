
score1 = input("중간 고사 점수 : ")
score2 = input("기말 고사 점수 : ")


if score1.isdigit() and score2.isdigit():
    score1 = int(score1)
    score2 = int(score2)

    totalScore = score1 + score2
    avgScore = totalScore / 2
    print("총점 : {}, 평균 : {}".format(totalScore, avgScore))

else:
    print('잘못 입력하셨습니다.')