minScore = 60
scores = (
    ('국어', 58),
    ('영어', 77),
    ('수학', 89),
    ('과학', 99),
    ('국사', 50))

for item in scores:
    if item[1] < minScore:
        print('과락 과목: {}, 점수: {}'.format(item[0], item[1]))

for subject, score in scores:
    if score < minScore:
        print('과락 과목: {}, 점수: {}'.format(subject, score))

for subject, score in scores:
    if score >= minScore: continue
    print('과락 과목: {}, 점수: {}'.format(subject, score))

# 과락 과목 출력
minScore = 60

korScore = int(input('국어 점수: '))
engScore = int(input('영어 점수: '))
matScore = int(input('수학 점수: '))
sciScore = int(input('과학 점수: '))
hisScore = int(input('국사 점수: '))

scores = (
    ('국어', korScore),
    ('영어', engScore),
    ('수학', matScore),
    ('과학', sciScore),
    ('국사', hisScore))

for subject, score in scores:
    if score < minScore:
        print('과락 과목: {}, 점수: {}'.format(subject, score))


# 학급 학생수가 가장 작은 학급과 가장 많은 학급 출력
studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
minclassNo = 0; maxclassNo = 0
minCnt = 0; maxCnt = 0
for classNo, cnt in studentCnts:
    if minCnt == 0 or minCnt > cnt:
        minclassNo = classNo
        minCnt = cnt

    if maxCnt < cnt:
        maxclassNo = classNo
        maxCnt = cnt

print('학생 수가 가장 적은 학급(학생수): {}학급({}명)'.format(minclassNo, minCnt))
print('학생 수가 가장 많은 학급(학생수): {}학급({}명)'.format(maxclassNo, maxCnt))