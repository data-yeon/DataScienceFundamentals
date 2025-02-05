class BmiAlgorithm:

    def __init__(self, w, h):
        self.BMISection = {18.5:['저체중', '정상'],
                           23:['정상','과체중'],
                           25:['과체중', '비만']}
        self.userWeight = w
        self.userHeight = h
        self.userBMI = 0
        self.userCondition = ''
        self.nearNum = 0
        self.minNum = 25
        

    def calculatorBMI(self):
        self.userBMI = round(self.userWeight / (self.userHeight * self.userHeight), 2)
        print(f'userBMI: {self.userBMI}')
    
    
    def printUserCondition(self):
        for n in self.BMISection.keys():
            absNum = abs(n - self.userBMI)
            if absNum < self.minNum:
                self.minNum = absNum
                self.nearNum = n
        print(f'self.nearNum: {self.nearNum}')

        if self.userBMI <= self.nearNum:
            self.userCondition = self.BMISection[self.nearNum][0]
        else:
            self.userCondition = self.BMISection[self.nearNum][1]
        print(f'self.userCondition: {self.userCondition}')
