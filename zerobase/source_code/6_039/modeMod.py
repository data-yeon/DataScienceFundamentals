import maxMod

class ModeAlgorithm:

    def __init__(self, ns, mn):
        self.nums = ns
        self.maxNum = mn
        self.indexes = []

    # 인덱스 리스트 생성 및 빈도 저장
    def setIndexList(self):
        self.indexes = [0 for i in range(self.maxNum + 1)]

        for n in self.nums:
            self.indexes[n] = self.indexes[n] + 1

    def getIndexList(self):
        if sum(self.indexes) == 0:
            return None
        else:
            return self.indexes

    def printAges(self):

        n = 1
        while True:

            maxAlo = maxMod.MaxAlgorithm(self.indexes)
            maxAlo.setMaxIdxAndNum()
            maxNum = maxAlo.getMaxNum()
            maxNumIdx = maxAlo.getMaxNumIdx()

            if maxNum == 0:
                break

            print(f'[{n:0>3}] {maxNumIdx}세 빈도수: {maxNum}\t', end='')
            print('+' * maxNum)
            self.indexes[maxNumIdx] = 0

            n += 1