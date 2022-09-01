"""
Create a class Vehicle add some attributes and methods to it
    - name
    - brand
    - wheels_count
    - engine_type
    - braking_system


Create a child class HeavyVehicle and inherit all the attributes from the parent class Vehicle
    - change the wheels_count from 4 to 6 in the initializer or accept the value while instantiating
    - add more instance attributes like max_load, mileage, etc.

Create a child class Bike and inherit all the attributes from the parent class Vehicle
    - change the wheels_count from 4 to 2 in the initializer
    - add setter or getter methods or property to add bike number, and owner name
    - try adding property instead of setter or getter for passenger/ pillion attribute

create different instances of Vehicle, HeavyVehicle, and Bike and check whether each other are subclasses
and instances of different classes or not.

"""

class Vehicle:
    wheels_count = 4
    engine = 'Diesel'
    braking_system = 'Drum Brakes'

    def __init__(self, name, brand) -> None:
        self.name = name
        self.brand = brand


class HeavyVehicle(Vehicle):
    def __init__(self, name, brand, max_load, mileage):
        super().__init__(name, brand)
        self.max_load = max_load
        self.milage = mileage
        self.wheels_count = 6


class Bike(Vehicle):
    def __init__(self, name, brand) -> None:
        super().__init__(name, brand)
        self.wheels_count = 2
        self.__number = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number
