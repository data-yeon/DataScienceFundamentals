class Car:

    def __init__(self, color, length):
        self.color = color
        self.length = length

    def doStop(self):
        print('STOP!!')

    def doStart(self):
        print('START!!')

    def printCarInfo(self):
        print(f'color: {self.color}')
        print(f'length: {self.length}')


car1 = Car('red', 200)
car2 = Car('blue', 300)

car1.printCarInfo()
car2.printCarInfo()




class AirPlane:

    def __init__(self, color, length, weight):
        self.color = color
        self.length = length
        self.weight = weight

    def takeOff(self):
        print('take-off')

    def landing(self):
        print('landing')

    def printAriPlaneInfo(self):
        print(f'color: {self.color}')
        print(f'length: {self.length}')
        print(f'weight: {self.weight}')

airPlane1 = AirPlane('red', 200, 2000)
airPlane2 = AirPlane('blue', 150, 2200)
airPlane3 = AirPlane('green', 180, 2100)
airPlane4 = AirPlane('white', 220, 1900)
airPlane5 = AirPlane('black', 210, 2300)

airPlane1.printAriPlaneInfo()
airPlane2.printAriPlaneInfo()
airPlane3.printAriPlaneInfo()
airPlane4.printAriPlaneInfo()
airPlane5.printAriPlaneInfo()
