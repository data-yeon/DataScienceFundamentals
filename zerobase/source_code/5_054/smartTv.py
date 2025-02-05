class NormalTv:

    def __init__(self, i=32, c='black', r='full-HD'):
        self.inch = i
        self.color = c
        self.resolution = r
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):
        print('TV power on!!')

    def turnOff(self):
        print('TV power off!!')

    def printTvInfo(self):
        print(f'inch: {self.inch}inch')
        print(f'color: {self.color}')
        print(f'resolution: {self.resolution}')
        print(f'smartTv: {self.smartTv}')
        print(f'aiTv: {self.aiTv}')


class Tv4k(NormalTv):

    def __init__(self, i, c, r='4k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s


class Tv8k(NormalTv):

    def __init__(self, i, c, r='8k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s

    def setAiTv(self, a):
        self.aiTv = a


if __name__ == '__main__':
    my4KTv = Tv4k('65', 'silver', '4K')
    my4KTv.setSmartTv('on')
    my4KTv.turnOn()
    my4KTv.printTvInfo()
    my4KTv.turnOff()

    my8KTv = Tv8k('75', 'black', '8K')
    my8KTv.setSmartTv('on')
    my8KTv.setAiTv('on')
    my8KTv.turnOn()
    my8KTv.printTvInfo()
    my8KTv.turnOff()
