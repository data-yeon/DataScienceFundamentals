from car_game import racing as rc
from car_game import car

myCarGame = rc.CarRacing()
car01 = car.Car('Car01', 'white', 250)
car02 = car.Car('Car02', 'black', 200)
car03 = car.Car('Car03', 'yellow', 220)
car04 = car.Car('Car04', 'red', 280)
car05 = car.Car('Car05', 'blue', 150)

myCarGame.addCar(car01)
myCarGame.addCar(car02)
myCarGame.addCar(car03)
myCarGame.addCar(car04)
myCarGame.addCar(car05)

myCarGame.startRacing()