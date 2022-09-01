"""
© https://sudipghimire.com.np


@property decorator in python classes

- They look like regular object variables but are capable of attaching custom behavior to the class.
- They are used as better alternative of getters and setters
- whenever we create a property inside a class, it's behavior will be tightly controlled.

for example we want to add a private variable to class and want to access and modify it.
I can achieve it using getter and setter method along with private variable.

or I can add getter, setter and deleter property so that I can access it
similar to attributes rather than calling methods.

structure:
class ABC:

    @property
    def my_property(self):
        # property body
"""


class Rectangle:

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        # self.__diagonal = (length**2 + breadth**2)**0.5


    # def get_length(self):
    #     return self.__length


    @property
    def length(self):
        return self.__length

    # def set_length(self, length):
    #     self.__length = length
    #     self.__diagonal = (self.__length**2 + self.__breadth**2)**0.5

    @length.setter
    def length(self, length):
        print('WARNING!! changing the length will also change the value of the diagonal')
        self.__length = length
        # self.__diagonal = (self.__length**2 + self.__breadth**2)**0.5

    # def get_diagonal(self):
    #     return self.__diagonal

    @property
    def diagonal(self):
        return (self.__length**2 + self.__breadth**2)**0.5


    def area(self):
        return self.__length * self.__breadth


r1 = Rectangle(3, 4)

# print(r1.get_length())
print(r1.length)

# r1.set_length(10)

r1.length = 10

# print('The diagonal is: ', r1.get_diagonal())
print('The diagonal is: ', r1.diagonal)


print(r1.diagonal)
