class Top5Players:

    def __init__(self, cts, ns):
        self.currentScores = cts
        self.newScore = ns

    def setAlignScore(self):
        nearIdx = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore - s)
            if absNum < minNum:
                minNum = absNum
                nearIdx = i

        if self.newScore >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores)-1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i-1]
            self.currentScores[nearIdx] = self.newScore

        else:
            for i in range(len(self.currentScores)-1, nearIdx+1, -1):
                self.currentScores[i] = self.currentScores[i-1]
            self.currentScores[nearIdx+1] = self.newScore

    def getFinalTop5Scroes(self):
        return self.currentScores
