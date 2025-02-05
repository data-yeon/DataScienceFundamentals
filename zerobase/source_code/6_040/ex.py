import nearMod

depth = int(float(input('input depth: ')))
print(f'depth: {depth}m')

na = nearMod.NearAlgorithm(depth)
temp = na.getNearNumber()
print(f'water temperature: {temp}도')