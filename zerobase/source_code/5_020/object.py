class Robot:

    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight

    def printRobotInfo(self):
        print('-' * 20)
        print(f'color: {self.color}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')
        print('-' * 20)


rb1 = Robot('red', 200, 80)
rb2 = Robot('blue', 300, 120)
rb3 = rb1

rb1.printRobotInfo()
rb2.printRobotInfo()
rb3.printRobotInfo()

rb1.color = 'gray'
rb1.height = 250
rb1.weight = 100

rb1.printRobotInfo()
rb2.printRobotInfo()
rb3.printRobotInfo()


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = list1

print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list1.append(6)
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list3[2] = 3.14
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list3 = list1.copy()
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list1[2] = 3.14
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')

list3[4] = 999
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'list3: {list3}')





scores = [int(input('국어 점수 입력: ')),
          int(input('영어 점수 입력: ')),
          int(input('수학 점수 입력: '))]

# print(scores)

copyScores = scores.copy()

for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print(f'이전 평균: {round(sum(scores) / len(scores), 2)}')
print(f'이후 평균: {round(sum(copyScores) / len(copyScores), 2)}')


