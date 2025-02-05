kor_avg = 88; eng_avg = 82; mat_avg = 90
sci_avg = 78; his_avg = 92

hong_kor_score = 85; hong_eng_score = 90; hong_mat_score = 82
hong_sci_score = 88; hong_his_score = 100

stu19cnt_kor_total = kor_avg * 20 - hong_kor_score
stu19cnt_eng_total = eng_avg * 20 - hong_eng_score
stu19cnt_mat_total = mat_avg * 20 - hong_mat_score
stu19cnt_sci_total = sci_avg * 20 - hong_sci_score
stu19cnt_his_total = his_avg * 20 - hong_his_score

stu19cnt_kor_avg = stu19cnt_kor_total / 19
stu19cnt_eng_avg = stu19cnt_eng_total / 19
stu19cnt_mat_avg = stu19cnt_mat_total / 19
stu19cnt_sci_avg = stu19cnt_sci_total / 19
stu19cnt_his_avg = stu19cnt_his_total / 19

kor_gap = hong_kor_score - stu19cnt_kor_avg
eng_gap = hong_eng_score - stu19cnt_eng_avg
mat_gap = hong_mat_score - stu19cnt_mat_avg
sci_gap = hong_sci_score - stu19cnt_sci_avg
his_gap = hong_his_score - stu19cnt_his_avg

print(f'국어 점수 차이: {"+" + str(round(kor_gap, 2)) if kor_gap > 0 else round(kor_gap, 2)}')
print(f'영어 점수 차이: {"+" + str(round(eng_gap, 2)) if eng_gap > 0 else round(eng_gap, 2)}')
print(f'수학 점수 차이: {"+" + str(round(mat_gap, 2)) if mat_gap > 0 else round(mat_gap, 2)}')
print(f'과학 점수 차이: {"+" + str(round(sci_gap, 2)) if sci_gap > 0 else round(sci_gap, 2)}')
print(f'국사 점수 차이: {"+" + str(round(his_gap, 2)) if his_gap > 0 else round(his_gap, 2)}')

stu19Cnt_total = stu19cnt_kor_avg + stu19cnt_eng_avg + stu19cnt_mat_avg + stu19cnt_sci_avg + stu19cnt_his_avg
stu19Cnt_avg = stu19Cnt_total / 5
hong_total = hong_kor_score + hong_eng_score + hong_mat_score + hong_sci_score + hong_his_score
hong_avg = hong_total / 5

avg_gap = round(hong_avg - stu19Cnt_avg, 2)
print(f'평균 차이: {"+" + str(round(avg_gap, 2)) if avg_gap > 0 else round(avg_gap, 2)}')