import maxAlgorithm, minAlgorithm
import nearAlgorithm

top5Scores = [9.12, 8.95, 8.12, 6.90, 6.18]
scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]
print(f'scores: {scores}')

maxA = maxAlgorithm.MaxAlgorithm(scores)
maxA.removeMaxScore()

minA = minAlgorithm.MinAlgorithm(scores)
minA.removeMinScore()

total = 0
average = 0

for n in scores:
    total += n

average = round(total / len(scores), 2)

print(f'total: {round(total, 2)}')
print(f'average: {average}')

tp = nearAlgorithm.Top5Players(top5Scores, average)
tp.setAlignScore()
top5Scores = tp.getFinalTop5Scroes()
print(f'top5Scores: {top5Scores}')

