# class NewGenerationPC:
#     def __init__(self, name, cpu, memory, ssd):
#         self.name = name
#         self.cpu = cpu
#         self.memory = memory
#         self.ssd = ssd
#
#     def doExcel(self):
#         print('EXCEL RUN!!')
#
#     def doPhotoshop(self):
#         print('PHOTOSHOP RUN!!')
#
#     def printPCInfo(self):
#         print(f'name: {self.name}')
#         print(f'cpu: {self.cpu}')
#         print(f'memory: {self.memory}')
#         print(f'ssd: {self.ssd}')
#
# myPc = NewGenerationPC('myPC', 'i5', '16G', '256G')
# friendPc = NewGenerationPC('friendPC', 'i7', '32G', '512G')
#
# myPc.printPCInfo()
# friendPc.printPCInfo()
#
# myPc.cpu = 'i9'
# myPc.memory = '64G'
# myPc.ssd = '1T'
#
# myPc.printPCInfo()
# friendPc.printPCInfo()



class Calculator:

    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def add(self):
        self.result = self.number1 + self.number2
        return self.result

    def sub(self):
        self.result = self.number1 - self.number2
        return self.result

    def mul(self):
        self.result = self.number1 * self.number2
        return self.result

    def div(self):
        self.result = self.number1 / self.number2
        return self.result


calculator = Calculator()
calculator.number1 = 10
calculator.number2 = 20

print(f'calculator.add(): {calculator.add()}')
print(f'calculator.sub(): {calculator.sub()}')
print(f'calculator.mul(): {calculator.mul()}')
print(f'calculator.div(): {calculator.div()}')



calculator.number1 = 3
calculator.number2 = 5

print(f'calculator.add(): {calculator.add()}')
print(f'calculator.sub(): {calculator.sub()}')
print(f'calculator.mul(): {calculator.mul()}')
print(f'calculator.div(): {calculator.div()}')
