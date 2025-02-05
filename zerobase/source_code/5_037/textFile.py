uri = 'C:/pythonTxt/'

file = open(uri + '5_037.txt', 'a')
file.write('python study!!')
file.close()


file = open(uri + '5_037.txt', 'r')
print(file.read())
file.close()


with open(uri + '5_037.txt', 'a') as f:
    f.write('python study!!')


with open(uri + '5_037.txt', 'r') as f:
    print(f.read())





import random

uri = 'C:/pythonTxt/'

def writeNumbers(nums):
    for idx, num in enumerate(nums):
        with open(uri + 'lotto.txt', 'a') as f:
            if idx < (len(nums) - 2):
                f.write(str(num) + ', ')
            elif idx == (len(nums) - 2):
                f.write(str(num))
            elif idx == (len(nums) - 1):
                f.write('\n')
                f.write('bonus: ' + str(num))
                f.write('\n')


rNums = random.sample(range(1, 46), 7)
print(f'rNums: {rNums}')

writeNumbers(rNums)

