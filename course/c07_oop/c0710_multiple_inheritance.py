"""
© https://sudipghimire.com.np

Multiple Inheritance.

Multiple inheritance means inheriting the behavior from 2 or more parent classes.

The structure would be

class A:
    <attributes>
    <methods>

class B:
    <attributes>
    <methods>

classs C(A, B):
    <attributes>
    <methods>

- In multiple inheritance, Python uses C3 Linearization algorithm to determine the order in which
  to resolve class attributes and methods. The process is also known as Method Resolution Order (MRO)

  To learn more about C3 linearization, you can check the link below:
  https://en.wikipedia.org/wiki/C3_linearization

"""

# Mixins


class Shop:
    reg_no = 0


class CoffeeShop(Shop):
    coffee_price = 30
    tea_price = 40


class Bakery(Shop):
    dough_nut_price = 10
    tea_price = 20


class Restaurant(CoffeeShop, Bakery):
    pizza_price = 20


print(Restaurant.tea_price)


r1 = Restaurant()

r1.milk_shake_price = 50

print(r1.milk_shake_price)

"""
© https://sudipghimire.com.np

Monkey Patching

- it is the process of adding new variable or method to a class after it's been defined
- we can introduce a new instance attribute to an object even after it has been initialized
- monkey patching is useful when we do not want to perform inheritance or create a child class and
  change the behavior of the previously defined classes or previously instantianted objects.

- if we monkey patch the instance attribute, it is not going to change the class template, instead
  it affects only the instance we've created
"""
