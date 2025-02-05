class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumCnt = 0

    def setMaxNum(self):
        self.maxNum = 0

        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n

    def getMaxNum(self):
        self.setMaxNum()

        return self.maxNum

    def setMaxNumCnt(self):
        self.setMaxNum()

        for n in self.nums:
            if self.maxNum == n:
                self.maxNumCnt += 1

    def getMaxNumCnt(self):
        self.setMaxNumCnt()

        return self.maxNumCnt

