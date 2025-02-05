passwds = ('password1234', 'abc123', 'qwerty', 'letmein', 'welcome00')
print(f'passwds : {passwds}')

scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))
total = 0

for s1 in scores:
    for s2 in s1:
        total += s2

total = round(total, 1)
avg = round((total / 6), 1)
print(f'3학년 총학점: {total}')
print(f'3학년 평균: {avg}')

print('-'*60)

grade4TagetScore = round((4.0 * 8 - total), 1)
print(f'4학년 목표 총학점: {grade4TagetScore}')

minScore = round(grade4TagetScore / 2, 1)
print(f'4학년 한학기 최소학점: {minScore}')

scores = list(scores)
scores.append((minScore, minScore))

print('-'*60)

scores = tuple(scores)
print(f'scores: {scores}')

