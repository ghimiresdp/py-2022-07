# def add(x, y):
#     return x + y

add = lambda x, y: x + y

print(add(5, 6))

hello_world = lambda: "Hello World"

print(hello_world())

z = lambda x, y: x**2 + y**2

print(z(3, 4))


def my_function(a, b):
    # print('I am inside function')
    return ((a + b) + ((a + b)**2)) // 2


# def odd_even(x):
#     return 'Even' if x%2==0 else 'Odd'
#     if x%2==0:
#         return 'Even'
#     else:
#         return 'Odd'

odd_even = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(odd_even(21))

lst = [1, 2, 3, 4, 5, 6]

lst_2 = lambda lst: [x**2 for x in lst]

print(lst_2(lst))
