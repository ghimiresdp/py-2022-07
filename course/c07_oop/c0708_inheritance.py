from abc import ABC, abstractmethod

# Inheritance
"""
# Inheritance
- This concept is exactly similar to biological inheritance where child inherits the feature of parent.
- In inheritance, there exists a parent class and child classes which inherits parent's behaviors.
- The base class will be the parent class and the class that is derived from the base class will
  be treated as a child class.

Basic Structure
class Parent:
    <attributes>
    <methods>

class Child(Parent):
    <attributes>
    <methods>
"""


class Temperature:
    pass


class Shape(ABC):        # Abstract Class

    @abstractmethod
    def area(self):
        print('Finding out the area of the shape')

    @abstractmethod
    def perimeter(self):
        print('Finding out the perimeter of the shape')


class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1415 * self.radius


class Triangle(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass


r1 = Rectangle(10, 5)

print(r1.area())
print(r1.perimeter())



sq1 = Square(5)

print(sq1.area())
print(sq1.perimeter())


print(isinstance(sq1, Rectangle))       # True
print(isinstance(sq1, Shape))           # True
print(isinstance(sq1, Temperature))     # False

print(isinstance(r1, Square))           # False (Parent is never instance of a child)

print(issubclass(Square, Rectangle))    # True
print(issubclass(Square, Shape))        # True
print(issubclass(Shape, Square))        # False


c1 = Circle(10)
print(c1.area())
print(c1.perimeter())
