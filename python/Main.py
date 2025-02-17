from car import Car
from account import Account
from uberX import UberX
from user import User

if _name_ == "_main_":
    print("Inicializando las info de los carros")
    
    print("Car")
    car = Car("AMS256", Account("Andres Herrera", "ASD12365", "munoshelensanchez@gmail.com", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberX = UberX("KL0365", Account("Marco Lois", "SGHJ1236", "marco munoshelensanchez@gmail.com", "7856"), "Toyota", "Corolla")
    
    print(vars(uberX))
    print(vars(uberX.driver))

    print("User")
    user = User("mariana Valle", "SDFG125F", "mariana@munoshelensanchez@gmail.com", "7856")
    print(vars(user))