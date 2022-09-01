"""
© https://sudipghimire.com.np

Types of methods:
- Bound
    - bound to the instance
    - bound to the class
- Unbound

# Class Methods and static methods

Class Methods
- Class methods are special kind of methods that are bound to the class instead of the instance
- If we create an instance and change the property of the object, it is not going to affect the property
  of the classmethod.

Static Methods
- Static methods are methods that do not bind to anything at all and simply return the underlying function
  without any transformation.
- They just behave like a function. Only the difference is they are called along with the class name.
"""


class Animal:
    legs = 4

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


    @classmethod
    def print_legs(cls):
        print('The number of legs is: ', cls.legs)

print(Animal.legs)
print(Animal.print_legs())

a1 = Animal('Dog')
a1.print_name()
a1.legs = 5
a1.print_legs()

a2 = Animal('Cow')

print(a1.name)


class Length:
    cm_inch_mul_factor = 2.54

    @classmethod
    def get_multiplication_factor(cls):
        return cls.cm_inch_mul_factor

    @staticmethod
    def cm_to_inches(cm):
        return cm / 2.54

    @staticmethod
    def inch_to_cm(inch):
        return inch * 2.54

    def __init__(self, cm) -> None:
        self.cm = cm

    def inches(self):
        return self.cm / self.get_multiplication_factor()

l1 = Length(30)
print(l1.inches())
l1.cm_inch_mul_factor = 5.54
print(l1.inches())


# print(Length.cm_to_inches(30))

# print(l1.cm_to_inches(l1.cm))
