uri = 'C:/pythonTxt/'

with open(uri + 'lans.txt', 'r') as f:
    lanList = f.readlines()

print(f'lanList: {lanList}')
print(f'lanList type: {type(lanList)}')





uri = 'C:/pythonTxt/'

with open(uri + 'lans.txt', 'r') as f:
    line = f.readline()

    while line != '':
        print(f'line: {line}', end='')
        line = f.readline()





scoreDic = {}

uri = 'C:/pythonTxt/'
with open(uri + 'scores.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tempList = line.split(':')
        scoreDic[tempList[0]] = int(tempList[1].strip('\n'))

        line = f.readline()

print(f'scoreDic: {scoreDic}')
