class NearAlgorithm:

    def __init__(self, d):
        self.temps = {0:24, 5:22, 10:20, 15:16, 20:13, 25:10, 30:6}
        self.depth = d
        self.nearNum = 0
        self.minNum = 24

    def getNearNumber(self):

        for n in self.temps.keys():
            absNum = abs(n - self.depth)
            if absNum < self.minNum:
                self.minNum = absNum
                self.nearNum = n

        return self.temps[self.nearNum]