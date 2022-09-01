def square(a, b, *other):
    _sum = a * a + b * b
    for item in other:
        _sum += item**2
    return _sum


print(square(1, 2))
print(square(1, 2, 3))
print(square(1, 2, 3, 4))
print(square(1, 2, 3, 4, 5, 6, 7))
print(square(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))


def square_1(*numbers):
    _sum = 0
    for item in numbers:
        _sum += item**2
    return _sum


print(square_1())
print(square_1(1))
print(square_1(1, 2))
print(square_1(1, 2, 3))
print(square_1(1, 2, 3, 4))
print(square_1(1, 2, 3, 4, 5, 6, 7))
print(square_1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))


def print_students(*args):
    for index, item in enumerate(args):
        print(index + 1, item, sep='\t')
    print()


print_students('John')
print_students('John', 'Jane')
print_students('John', 'Jane', 'Jennifer')
"""
Output:

1   John
2   Jane
...

n   xyz
"""


def print_detail(name, age, **other):
    print(f'name is {name}')
    print(f'age is {age}')
    for key, value in other.items():
        print(f'{key} is {value}')
    print()


print_detail('John', 20)
print_detail(20, 'John')

print_detail(age=20, name='John')
print_detail(age=20, name='John', dob='1999-12-12')
print_detail(
    'John',
    20,
    dob='1999-12-12',
    father='Spock',
    address='USA',
)

# print(square_1(*range(1, 1001)))

# list_1 = [1, 3, 5, 7, 9]
# print(square_1(*list_1))

students = [
    {'name': 'John Doe', 'age': 20, 'subject': 'Music'},
    {'name': 'John Lennon', 'age':30, 'subject': 'Music'},
    {'name': 'John Legend', 'age': 40, 'subject': 'Music'},
    {'name': 'John Mayer', 'age': 50, 'subject': 'Music'},
]

for student in students:
    print_detail(**student)


# while True:
#     print('abc')
#     x+=1
#     if (some_condition):
#         break


def _func(a, b, *args, c=0, **kwargs):
    pass
