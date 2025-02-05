class LottoMode:

    def __init__(self, ln):
        self.lottoNums = ln
        self.modeList = [0 for n in range(1, 47)]

    def getLottoNumMode(self):

        for roundNums in self.lottoNums:
            for num in roundNums:
                self.modeList[num] = self.modeList[num] + 1

        return self.modeList

    def printModeList(self):
        if sum(self.modeList) == 0:
            return None

        for i, m in enumerate(self.modeList):
            if i != 0:
                print(f'번호: {i:>2}, 빈도: {m}, {"*" * m}')
