import mod

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74,
          54, 73, 88, 70, 68, 50, 95, 89, 69, 98]

score_avg = mod.getAvg(scores)
score_max = mod.getMax(scores)
deviation = mod.getDeviation(score_avg, score_max)

print(f'score_avg: {score_avg}')
print(f'score_max: {score_max}')
print(f'deviation: {deviation}')
