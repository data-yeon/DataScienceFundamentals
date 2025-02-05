import rankMod as rm
import random

midStuScos = random.sample(range(50, 101), 20)
endStuScos = random.sample(range(50, 101), 20)

rd = rm.RankDeviation(midStuScos, endStuScos)

rd.setMidRank()
print(f'midStuScos: {midStuScos}')
print(f'mid_rank: {rd.getMidRank()}')

rd.setEndRank()
print(f'endStuScos: {endStuScos}')
print(f'end_rank: {rd.getEndRank()}')

rd.printRankDeviation()