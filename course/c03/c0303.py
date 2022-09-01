# Tuple

# %%
tup_1 = ()

print(type(tup_1))

# %%
tup_2 = (1, 2, 3, 4)
print(tup_2)
print(type(tup_2))

# %%
tup_3 = (1, 3, 'john', 4.5, True)
print(tup_3)

# %%
list_1 = [
    1,
    2,
    3,
    4,
]

tup_4 = tuple(list_1)
print(tup_4)

# %%
lst_1 = ['john']
print(lst_1)
type(lst_1)
# %%
tup = ('Hello there I am John '
       'Doe and I am from '
       'New York.')

print(tup)
type(tup)

# %%
people = ('john', )
print(people)
print(type(people))

# %%

y = (10.5, )

print(type(y))

# %%
tuple_1 = ()  # creates an empty tuple

tuple_2 = (1, )  # creates a tuple with only one element

tuple_3 = (1, 2, 3)  # creates a tuple containing 1, 2, 3

tuple_4 = tuple([1, 2, 3])  # creates a tuple from a list [1, 2, 3]

# a tuple with items organized in multiple lines
tuple_5 = (
    'cow',
    'buffalo',
    'goat',
    'tiger',
    'leopard',
    'lion',
    'cat',
    'dog',
)

# A tuple containing random data types
tuple_6 = (1, 'John', 'Moon', True, 45.62)

t1: tuple = (1, 2, 3)  # type hinting for tuple

# %%
numbers = (-2, 47, 53, 1, 2, 3, 7, 8)

print(numbers[2])

print(numbers[3])

print(numbers[1:4])

print(numbers[-4:-1])

print(numbers[0:9:2])
print(numbers[::2])
#

# %%
odd = (1, 3, 5, 7, 9, 11, 13, 15, 16)

# odd = list(odd)
# # odd.remove(16)
# # odd.append(17)
# # odd[-1] = 17

# odd = tuple(odd)

# # odd = tuple(list(odd[:-1] ) + [17])
# odd = odd[:-1] + (17,)

odd = (*odd[:-1], 17, 19)
print(odd)

# %%

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
t1 = t3
print(t1)
# %%

x = [1, 2, 3]
y = [4, 5, 6]

z = *x, *y

print(z)
# 1, 2, 3, 4, 5, 6

# %%
x = [1, 2, 3, 7, 8, 9]

# x.insert(3, 4)
# x.insert(4, 5)
# x.insert(5, 6)

# x = x[0:3] + [4, 5, 6] + x[3:]
x = [*x[:3], 4, 5, 6, *x[3:]]

print(x)

#

# %%
