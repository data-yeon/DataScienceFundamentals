class Car01:

    def drive(self):
        print('drive() method called!!')


class Car02:

    def turbo(self):
        print('turbo() method called!!')

class Car03:

    def fly(self):
        print('fly() method called!!')


class Car(Car01, Car02, Car03):

    def __int__(self):
        pass

myCar = Car()

myCar.drive()
myCar.turbo()
myCar.fly()



class BasicCalculator:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

class DeveloperCalculator:

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2


class Calculator(BasicCalculator, DeveloperCalculator):

    def __int__(self):
        pass

myCal = Calculator()
print(f'myCal.add(10, 20): {myCal.add(10, 20)}')
print(f'myCal.sub(10, 20): {myCal.sub(10, 20)}')
print(f'myCal.mul(10, 20): {myCal.mul(10, 20)}')
print(f'myCal.div(10, 20): {myCal.div(10, 20)}')

print(f'myCal.mod(10, 3): {myCal.mod(10, 3)}')
print(f'myCal.flo(10, 3): {myCal.flo(10, 3)}')
print(f'myCal.exp(10, 3): {myCal.exp(10, 3)}')

