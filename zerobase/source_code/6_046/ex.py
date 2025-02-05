datas = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
print(f'datas: {datas}')

ascIIDatas = []
for data in datas:
    if str(data).isalpha():
        ascIIDatas.append(ord(data))
        continue

    ascIIDatas.append(data)

print(f'ascIIDatas: {ascIIDatas}')


ranks = [0 for i in range(len(ascIIDatas))]

for idx, data1 in enumerate(ascIIDatas):
    for data2 in ascIIDatas:
        if data1 < data2:
            ranks[idx] += 1

print(f'ranks: {ranks}')

for i, d in enumerate(datas):
    print(f'data:{d:>2} \t rank:{ranks[i] + 1}')