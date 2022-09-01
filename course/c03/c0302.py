list_1 = ['Atanasoff', 'Berry', 'Calculator']

# the last item should be Computer, so I need to change it

third_value = list_1[2]

list_1[2] = 'Computer'

print(list_1)

# ['Atanasoff', 'Berry', 'Computer']
list_1[1] = 'apple'
print(list_1)

list_1[-3] = 'John'

print(list_1)

list_1 = ['Atanasoff', 'Berry', 'Calculator']

prime = [2, 3, 5, 6, 12, 13, 17]
# I wrote 6, 12 instead of 7, 11 by mistake so I want to change them
# prime[3] = 7
# prime[4] = 11

prime[3:5] = [7, 11]  # equivalent to previous commented lines
print(prime)
# [2, 3, 5, 7, 11, 13, 17]

prime = [2, 3, 5, 6, 12, 17]
# I wrote 6, 12 instead of 7, 11 by mistake and I also forgot to include 13
# so I want to change [6, 12] by [7, 11, 13]
# prime[3:5] -> [6, 12]

prime[3:5] = [7, 11, 13]
print(prime)

odd_num = [1, 3, 5, 7, 8, 10, 15, 17]
print(len(odd_num))
odd_num[4:6] = [9, 11, 13]

print(odd_num)

print(len(odd_num))

print(odd_num.__len__())

# Adding an element/elements to a list

# append
# insert
# extend

animals = ['cat', 'dog', 'tiger']
animals.append('monkey')
print(animals)
# ['cat', 'dog', 'tiger', 'monkey']
animals.append('donkey')
print(animals)

animals.insert(1, 'Elephant')
print(animals)
animals.insert(0, 'cow')
print(animals)

animals.extend(['ape', 'bear', 'antelope'])
print(animals)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

l1.extend(l2)
print(l1)

l1 += l2
print(l1)

l2.extend(l1)
print(l2)

l3 = l1 + l2
print(l3)

l4 = [*l1, *l2]
print(l4)

# Removing item / items from the list

even = [2, 4, 6, 8, 10, 12, 14]

value = even.pop()
print(even)
print(f'The popped out value is: {value}')

value = even.pop()
print(even)
print(f'The popped out value is: {value}')

# popping out from an empty list throws out an error
xyz = []
# xyz.pop()

even = [2, 4, 6, 8, 10, 12, 14]

value = even.pop(2)  # 2 is the index of 6
print(even)
print('Popped out value is: ', value)

# [2, 4, 8, 10, 12, 14]
value = even.pop(3)  # 3 is the index of 10 now
print(even)
print('Popped out value is: ', value)

# [2, 4, 8, 12, 14]
value = even.pop(-1)  # -1 is the negative index of 14 now
print(even)
print('Popped out value is: ', value)

# [2, 4, 8, 12]
# value = even.pop(4)  # IndexError is raised because of insufficient items

#
fib = [1, 1, 2, 3, 5, 8, 13, 21]

# value = fib.remove(13)    #it does not return value
# print(value)      None
fib.remove(13)  # it does not return value
print(fib)

even = [2, 4, 8, 2, 10, 2, 6, 2]
even.remove(2)
print(even)

even.remove(2)
print(even)

# even.remove(12)   # ValueError

del even[1], even[3]
print(even)

# clearing all items from the list

even.clear()  # []
print(even)

even = [2, 4, 8, 2, 10, 2, 6, 2]
del even[2:5]
print(even)

x = 5
y = 10
print(x)
del x, y

# print(x)

even *= 0
print(even)

# Copy method

a = 5
b = a

b += 2

print(a)
print(b)

x = [4, 5, 6, 7, 8]
y = x.copy()

y.pop()

print(x)
print(y)

#

# x = list(range(10000000))

# #
# y = x
# j = x
# k = x
# l= x
# m = x
# n = x
# o = x
# #
# z = x.copy()
# za = x.copy()
# zb = x.copy()
# zc = x.copy()

# #
# del z, za, zb, zc

# reversing the list
lst = [4, 2, 9, 0, 1, 13, 76, -421, -5, 66]

# print(lst[::-1])

lst.reverse()
print(lst)

# using slice
lst = lst[::-1]

print(lst)

lst = [4, 2, 9, 0, 1, 13, 76, -421, -5, 66]

# method 1
lst.sort(reverse=True)
print(lst)

# method 2
new_lst = sorted(lst, reverse=True)
print(lst)
print(new_lst)

# finding out the index
prime = [2, 3, 5, 13, 7, 11, 13, 17, 19, 13, 23]

print(prime.index(13))      # 3
print(prime.index(13, 4))   # 6
print(prime.index(13, 7))

# Counting the number of items
print(prime.count(13))
