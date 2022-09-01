# Relational Operations

"""
Relational Operations

    equals  (==)
    not equals(!=)
    less than   (<)
    less than or equals (<=)
    greater than    (>)
    greater than or equals  (>=)

Relational operation always returns either True or False
"""

x = 5

print(x == 6)
# a = int(input("Enter any number: "))
a = 12
print(f'The number is odd: {a%2 == 1}')


print('Divisible by both 2 and 3: ', a%2 == a%3 == 0)
#

# not equals( != )
print(5 != 6)  # True
print(4 + 1 != 6 - 1)  # False


#
print(4 < 5)  # True
print(4 < 4)  # False
print(5 < 4)  # False

print(4 <= 5)  # True
print(4 <= 4)  # True
print(5 <= 4)  # False

# greater than    ( > )
print(4 > 5)  # False
print(4 > 4)  # False
print(5 > 4)  # True
print('test: ', 'A' > 'a') # True

print(4 >= 5)  # False
print(4 >= 4)  # True
print(5 >= 4)  # True


print(ord('a'))
