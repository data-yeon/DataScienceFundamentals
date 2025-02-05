import random

scores = random.sample(range(50, 101), 20)
ranks = [0 for i in range(20)]

for idx, sco1 in enumerate(scores):
    for sco2 in scores:
        if sco1 < sco2:
            ranks[idx] += 1

print(scores)
print(ranks)

for i, s in enumerate(scores):
    print(f'score:{s} \t rank:{ranks[i] + 1}')
