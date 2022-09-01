"""
Sets

- Sets are similar to lists except they have unique data
- Sets are represented by braces {}
- Sets are not ordered
- Sets can not be accessed with indices.
- Set items can not be changed individually, but can be added to it

- Mathematical operations
    - Union
    - Intersection
    - Difference, ...


"""
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7, 11}
empty = set()
animals = {'Tiger', 'Leopard', 'Lion', 'tiger'}

print(odd)
print(type(odd))
print(type(empty))

# Duplicates are discarded but does not give error
odd = {1, 3, 5, 7, 9, 11, 1, 9, 1, 9, 1, 1}

print(odd)

print(animals)
#

odd = {15, 1, 3, 5, 7, 9, 11}

print(odd.pop())
odd.add(13)
print(odd)

odd.update([15, 17, 19])
print(odd)

x = odd.pop()
print(x)

print(animals.pop())

odd = {1, 3, 5, 7, 9, 11}

odd.discard(5)  # discards 5
odd.discard(15)  # does nothing
print(odd)

odd.remove(7)  # discards 7
# odd.remove(17)    # throws error when no items are present
# print(odd)

#
print('Length: ', len(odd))

print('Length: ', odd.__len__())

for x in odd:
    print(x)

#
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7, 11}

# Intersection [ A n B ]
# The numbers that are both odd and prime

print(odd.intersection(prime))
print(prime.intersection(odd))

print(odd & prime)

# Union [ A U B ]
# The numbers that are either odd or prime
print(odd.union(prime))
print(prime.union(odd))

print(odd | prime)

#
# odd = {1, 3, 5, 7, 9, 11}
# prime = {2, 3, 5, 7, 11}

print(odd.difference(prime))
print(odd - prime)

print(prime.difference(odd))

print(prime - odd)

print(odd.symmetric_difference(prime))
print(prime.symmetric_difference(odd))

print(prime ^ odd)

#
domestic = {'cow', 'cat', 'dog', 'rabbit', 'goat'}
carnivor = {'tiger', 'cat', 'dog', 'wolf', 'lion'}

# I want animals that are both domestic and carnivorous
print(domestic & carnivor)  # Intersection

# I want animals that are domestic but not carnivorous
print(domestic - carnivor)  # difference

# I want animals that are either domestic or carnivorous
# print(domestic.union(carnivor))
print(domestic | carnivor)  # Union

# I want animals that are either domestic or carnivorous but not both
# (A - B) U (B - A)
print(domestic ^ carnivor)  # Symmetric Difference
print((domestic - carnivor) | (carnivor - domestic))

# I want animals that are carnivorous but not domestic
# & - | ^
print(carnivor - domestic)

odd = {1, 3, 5, 7, 9, 11}
prime = {3, 5, 7, 11}

print(prime.issubset(odd))
print(odd.issubset(prime))

print(prime.issuperset(odd))
print(odd.issuperset(prime))

#
odd = {3, 5, 7, 11}
prime = {3, 5, 7, 11}

print(prime.issubset(odd))
print(odd.issubset(prime))

print(prime.issuperset(odd))
print(odd.issuperset(prime))

#
odd = {1, 3, 5, 7}
even = {2, 4, 6, 8}

print(odd.isdisjoint(even))

#
x = [1, 3, 5, 7, 9, 3, 7, 3, 1, 3, 5, 11]
print(x)
x = set(x)
print(x)

# Write a program to find out the unique values from the list below.
# The program should have the final value as a list

x = [1, 3, 5, 7, 9, 3, 7, 3, 1, 3, 5, 11]
x = list(set(x))

print(x)

#
x = {1, 3, 5, 7}
x.add(9)

y = frozenset([1, 3, 5, 7, 9, 11, 7])

print(y)
y.union(x)

#
x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#
# x = x.difference({7, 8, 9, 10})
y = x - {7, 8, 9, 10}

# x = x.union({11, 12, 13, 14})
z = x | {11, 12, 13, 14}
print(x)
print(y)
print(z)
