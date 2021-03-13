import importlib
import sys

db = importlib.import_module("Mysql")
db = db.Mysql()
cars = db.getCars()
routes = db.getRoute()

print("Введите номер автомобиля:")
print("№ | Марка | Расход")
for car in cars:
   print(car['id'], " | ", car['name'], " | ", car['comsumption'], "л.")

numberCar = input()
car = db.getCarById(numberCar)
if car is None:
   print('Машины №', numberCar, 'не найдена')
   sys.exit()

print('Выберите номер маршрута')
print('№ | Название | Дистанция')
for route in routes:
   print(route['id'], " | ", route['name'], " | ", route['distantion'], "км.")

numberRoute = input()
route = db.getRouteById(numberRoute)
if route is None:
   print('Маршрут №', numberRoute, 'не найдена')
   sys.exit()

resultOil = car['comsumption']/100*route['distantion']
print("Ваш расход под данному маршруту равен", resultOil)
print("Программа завершена")
sys.exit()