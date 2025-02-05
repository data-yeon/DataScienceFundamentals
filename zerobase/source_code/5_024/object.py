class MidExam:

    def __init__(self, s1, s2, s3):
        print('[MidExam] __init__()')

        self.mid_kor_score = s1
        self.mid_eng_score = s2
        self.mid_mat_score = s3

    def printScores(self):
        print(f'mid_kor_score: {self.mid_kor_score}')
        print(f'mid_eng_score: {self.mid_eng_score}')
        print(f'mid_mat_score: {self.mid_mat_score}')

class EndExam(MidExam):

    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[EndExam] __init__()')

        super().__init__(s1, s2, s3)

        self.end_kor_score = s4
        self.end_eng_score = s5
        self.end_mat_score = s6

    def printScores(self):
        super().printScores()
        print(f'end_kor_score: {self.end_kor_score}')
        print(f'end_eng_score: {self.end_eng_score}')
        print(f'end_mat_score: {self.end_mat_score}')

    def getTotalScore(self):
        total = self.mid_kor_score + self.mid_eng_score + self.mid_mat_score
        total += (self.end_kor_score + self.end_eng_score + self.end_mat_score)

        return total

    def getAverageScore(self):
        return self.getTotalScore() / 6

exam = EndExam(85, 90, 88, 75, 85, 95)
exam.printScores()
print(f'Total: {exam.getTotalScore()}')
print(f'Average: {round(exam.getAverageScore(), 2)}')