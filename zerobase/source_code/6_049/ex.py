import mod

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74,
          54, 73, 88, 70, 68, 50, 95, 89, 69, 98]

scores_avg = mod.getAvg(scores)
scores_min  = mod.getMaxOrMin(scores, maxFlag=False)
deviation =  mod.getDeviation(scores_avg, scores_min)

print(f'scores_avg: {scores_avg}')
print(f'scores_min: {scores_min}')
print(f'deviation: {deviation}')

import mod2

sm = mod2.ScoreManagement(scores)
print(f'score_avg: {sm.getAvgScore()}')
print(f'score_min: {sm.getMinScore()}')
print(f'score_max: {sm.getMaxScore()}')
print(f'score_min_deviation: {sm.getMinDeviation()}')
print(f'score_max_deviation: {sm.getMaxDeviation()}')

