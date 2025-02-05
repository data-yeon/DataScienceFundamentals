from abc import ABCMeta
from abc import abstractmethod

# class AirPlane(metaclass=ABCMeta):
#
#     @abstractmethod
#     def flight(self):
#         pass
#
#     def forward(self):
#         print('전진!!')
#
#     def backward(self):
#         print('후진!!')
#
#
# class Airliner(AirPlane):
#
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 400km/h 비행!!')
#
#
# class fighterPlane(AirPlane):
#
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 700km/h 비행!!')
#
#
# ap1 = Airliner('red')
# ap1.flight()
# ap1.forward()
# ap1.backward()
#
#
# ap2 = fighterPlane('blue')
# ap2.flight()
# ap2.forward()
# ap2.backward()


class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass


class ChildCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

childCal = ChildCalculator()
childCal.add(10, 20)
childCal.sub(10, 20)
childCal.mul(10, 20)
childCal.div(10, 20)


class DeveloperCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

    def mod(self, n1, n2):
        print(n1 % n2)

    def flo(self, n1, n2):
        print(n1 // n2)


devCal = DeveloperCalculator()
devCal.add(10, 20)
devCal.sub(10, 20)
devCal.mul(10, 20)
devCal.div(10, 20)
devCal.mod(10, 20)
devCal.flo(10, 20)
