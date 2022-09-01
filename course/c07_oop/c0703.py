# Encapsulation
"""
© https://sudipghimire.com.np

Encapsulation

- It is the process of restricting the direct access to the data.
- Encapsulation is achieved by binding the data along with methods to make the data usable.
- When the attribute becomes private, we do not have direct access to the data that time we use
  getters and setters to retrieve and set the value to the variable.

Encapsulation in Python.

Encapsulation can be achieved using the following methodologies in python:
1. Getters and Setters
2. Property
"""
# Getters and Setters
"""
- whenever we need to access private attributes, we need to create the helper function that has access to those
  attributes. The helper functions can get or set values of the attribute.
- getter generally takes no parameter and setter takes at least one parameter except self parameter


Why do we use Getters and setters instead of public variables?

- It helps achieving encapsulation which helps hiding or modifying the state of the structured data
  preventing the unauthorized access.
- Suppose changing the state of an object should change another attributes and if we give them accessing the state,
  then the program should behave abnormally.
- It helps avoiding mistakes when we want to change the state when we want to change states repeatedly.

"""


class Rectangle:
    # public
    pubic = 0
    # protected
    _protected = 10
    # private
    __private = 0

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        self.__diagonal = (length**2 + breadth**2)**0.5

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length
        self.__diagonal = (self.__length**2 + self.__breadth**2)**0.5

    def get_diagonal(self):
        return self.__diagonal

    def area(self):
        return self.__length * self.__breadth


r1 = Rectangle(3, 4)

print(r1.get_length())
print('The diagonal is: ', r1.get_diagonal())

# logically, r1.__length = 8
r1.set_length(8)
print('The diagonal is: ', r1.get_diagonal())

# print(r1.diagonal)
print(r1._protected)

print(r1._Rectangle__length)

r1.pubic = 10
