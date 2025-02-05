class Robot:

    def __init__(self, c, h ,w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('총알 발사!!')

    def printRobotInfo(self):
        print(f'color: {self.color}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')


class NewRobot(Robot):

    def __init__(self, c, h ,w):
        super().__init__(c, h, w)

    def fire(self):
        super().fire()
        print('레이저 발사!!')

myRobot = NewRobot('blue', 200, 300)
myRobot.printRobotInfo()
myRobot.fire()


class TriangleArea:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTriangleAreaInfo(self):
        print(f'width: {self.width}')
        print(f'height: {self.height}')

    def getArea(self):
        return self.width * self.height / 2

class NewTriangleArea(TriangleArea):

    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        return str(super().getArea()) + '㎠'

ta = NewTriangleArea(7, 5)
ta.printTriangleAreaInfo()
triangleArea = ta.getArea()
print(f'TriangleArea: {triangleArea}')
