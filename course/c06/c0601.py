# def my_function():
#     print("I am printing out the values")

# print('I am outside of the function')
# my_function()

# x = 5
# my_function()
# x = 5
# my_function()

# x = 5
# my_function()


def empty_function():
    pass


def say_hi():
    return 'Hi there!!'


x = say_hi()  # x will have value of 'Hi there!!'

print(say_hi().upper())
# directly prints 'Hi there!!' since it is returned and passed as an argument to
# another function `print()`

# print(x)

# def my_function():
#     print("I am printing out the values")

# x = my_function()
# print(x)    # None


def add_me(num_1, num_2):
    result = num_1 + num_2
    return result


result_1 = add_me(4, 5)
print(result_1)  # 9

result_2 = add_me(10, 5)
print(result_2)  # 15

print(add_me(50, 49))
"""
Write a program that accepts the following:

- a principal amount (p)
- time in years (t)
- rate of interest in percentage (r)

and calculates the simple interest and returns the result
"""


def si(p: int, t: int, r: float) -> float:
    return p * t * r / 100


# si_1 = 1000 + 2 * 10 / 100
si_1 = si(1000, 2, 10.0)
print(si_1)

# si_2 = 5000 + 3 * 20 / 100
si_2 = si(5000, 3, 20.0)
print(si_2)
"""
Write a program that accepts the following:

- a principal amount (p)
- time in years (t)
- rate of interest in percentage (r)

and calculates the simple interest and returns the result
Given condition:
if time is greater than 5 years, you need to add additional 2% of the service
"""

# def simple_interest(p: int, t: int, r: float) -> float:
#     if t > 5:
#         return p * t * r / 100 + p * 2 / 100
#     return p * t * r / 100


def simple_interest(p: int, t: int, r: float) -> float:
    additional = 0
    if t > 5:
        additional = 2
    return p * (t * r + additional) / 100


# si_1 = 1000 + 2 * 10 / 100
si_1 = simple_interest(1000, 10, 10.0)
print('The simple interest is: ', si_1)

# if rate is increased for all years
# def simple_interest(p: int, t: int, r: float) -> float:
#     if t > 5:
#         r = r + 2
#     return p * t * r / 100

# si_3 = simple_interest(1000, 2)
# TypeError: simple_interest() missing 1 required positional argument: 'rate'

# si_3 = simple_interest(1000, 2, 10, 5)
#TypeError: simple_interest() takes 3 positional arguments but 4 were given


def double_triple(number):
    if number % 2 == 0:
        return 2 * number
    return 3 * number


print(double_triple(4))  # 8
print(double_triple(5))  # 15

# functions can also be used in comprehensions
list_1 = [double_triple(n) for n in range(1, 11)]
print(list_1)
# [3, 4, 9, 8, 15]

# Write a program that returns the simple interest and an amount from the above solution


def simple_interest_amount(p: int, t: int, r: float) -> tuple:
    si = p * t * r / 100
    sa = si + p
    return si, sa


si_2, sa_2 = simple_interest_amount(1000, 2, 20)

print(si_2)
print(sa_2)


# Default Parameters
# Write a program that returns the simple interest given that,
# if rate is not given, the default rate is 12%
def interest(p, t, r=12):
    si = p * t * r / 100
    return si


print(interest(1000, 2, 15))
print(interest(1000, 2))

# write a function tha takes either 2 or 3 numbers and returns
# the sum of squares of those numbers


def square(a, b, c=0, d=0):
    return a * a + b * b + c * c + d * d


print(square(1, 2))
print(square(1, 2, 3))
print(square(1, 2, 3, 4))
print(square(1, 2, 3, 4, 5, 6, 7))
