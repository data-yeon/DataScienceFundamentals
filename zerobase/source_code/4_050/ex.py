dic = {}

for n in range(3, 11):
    hap = 180 * (n - 2)
    ang = int(hap / n)
    dic[n] = [hap, ang]

print(dic)



dic = {}

for n1 in range(2, 11):
    tempList = []
    for n2 in range(1, n1+1):
        if n1 % n2 == 0:
            tempList.append(n2)
    dic[n1] = tempList

print(dic)

