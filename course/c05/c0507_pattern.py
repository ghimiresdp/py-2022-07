"""
A A A A A
A A A A A
A A A A A
A A A A A
A A A A A
"""

for i in range(5):
    for j in range(5):
        print('A', end=' ')
    print()


"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(5):
        print(i, end=' ')
    print()

print()
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
for i in range(5):
    for j in range(1, 6):
        print(j, end=' ')
    print()


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()


"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

Row 1: 5 ....1
Row 2: 5 ...2
Row 3: 5...3
Row i: 5..i
"""
print('some pattern')
for i in range(5):
    for j in range(5, i, -1):
        print(j, end=' ')
    print()

print('some new pattern')
for i in range(5, 0, -1):
    for j in range(5, 5-i, -1):
        print(j, end=' ')
    print()
