class TemCls:

    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printClsInfo(self):
        print(f'self.number: {self.number}')
        print(f'self.str: {self.str}')


# 얕은 복사
tc1 = TemCls(10, 'Hello')
tc2 = tc1

tc1.printClsInfo()
tc2.printClsInfo()

tc2.number = 3.14
tc2.str = 'Bye'

tc1.printClsInfo()
tc2.printClsInfo()



# 깊은 복사
import copy

tc1 = TemCls(10, 'Hello')
tc2 = copy.copy(tc1)

tc1.printClsInfo()
tc2.printClsInfo()

tc2.number = 3.14
tc2.str = 'Bye'

tc1.printClsInfo()
tc2.printClsInfo()


# 리스트 깊은 복사
import copy

scores = [9, 8, 5, 7, 6, 10]
scoresCopy = []


scoresCopy = scores
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


for s in scores:
    scoresCopy.append(s)
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


scoresCopy.extend(scores)
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


scoresCopy = scores.copy()
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')


scoresCopy = scores[:]
print(f'id(scores): {id(scores)}')
print(f'id(scoresCopy): {id(scoresCopy)}')




plaOriSco = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
plaCopSco = plaOriSco.copy()

plaOriSco.sort()

plaCopSco.sort()
plaCopSco.pop(0)
plaCopSco.pop()

print(f'plaOriSco: {plaOriSco}')
print(f'plaCopSco: {plaCopSco}')


oriTot = round(sum(plaOriSco), 2)
oriAvg = round(oriTot / len(plaOriSco), 2)
print(f'Original Total: {oriTot}')
print(f'Original Average: {oriAvg}')

copTot = round(sum(plaCopSco), 2)
copAvg = round(oriTot / len(plaCopSco), 2)
print(f'Copy Total: {copTot}')
print(f'Copy Average: {copAvg}')


print(f'oriAvg - copAvg: {oriAvg - copAvg}')




