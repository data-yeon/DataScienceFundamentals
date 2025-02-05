class MinAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0
        self.minNumCnt = 0

    def setMinNum(self):
        self.minNum = 51

        for n in self.nums:
            if self.minNum > n:
                self.minNum = n

    def getMinNum(self):
        self.setMinNum()

        return self.minNum

    def setMinNumCnt(self):
        self.setMinNum()

        for n in self.nums:
            if self.minNum == n:
                self.minNumCnt += 1

    def getMinNumCnt(self):
        self.setMinNumCnt()

        return self.minNumCnt

