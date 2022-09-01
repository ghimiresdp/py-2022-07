class House:
    build_method = 'concrete'   # Class Attribute

    def __init__(self, rooms, stories):
        # self.build_method = 'concrete'  # Instance Attribute
        self.rooms = rooms          # Instance Attribute
        self.stories = stories

print(House.build_method)
my_house = House(rooms=5, stories=3)
friends_house = House(rooms=4, stories=5)


print(my_house.rooms)
# my_house.build_method = 'wooden'
print(my_house.build_method)

print(friends_house.rooms)
print(friends_house.build_method)

House.build_method = 'unspecified'

print(my_house.build_method)


###############################################################
# Create a Rectangle class and find out area for different dimensions

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

rect_1 = Rectangle(3, 5)
print(rect_1.length)
print(rect_1.area())

rect_2 = Rectangle(2, 10)
print(rect_2.area())



class Laptop:
    """
    This class can be used to initialize a laptop instance.
    The instance attributes "make", "model", "price" are mandatory

    If some of the laptops have different configuration, then
    we can change the class attributes "touchpad" and "nipple"
    after initialization.
    """
    touchpad = True
    nipple = False

    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f'<Laptop: {self.make} {self.model}>'


l1 = Laptop('HP', 'Spectre', 1000)
print(l1.touchpad)

l2 = Laptop('Dell', 'Vostro', 1200)

l3 = Laptop('Lenovo', 'Thinkpad', 1200)
l3.nipple = True


# print(l1.nipple)  # accessing the class attribute
# print(l3.nipple)            # accessing the instance attribute since class attribute is overridden

# print(Laptop.nipple)        # accessing the class attribute

print(l1.make)
print(l1)
print(l2)
print(l3.__dict__)


print (l1.__doc__)

print(l1.__sizeof__())


x: int = 5

print(type(x))
