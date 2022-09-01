# Nesting

# Nesting is the process of adding an iterable inside another iterable

x = [1, 2, 3, 'ram', [5, 6], 7, 8]
value = x[3][0]

print(value)

print(x[4][0])

# I want to create a matrix
# scalar        x = 5
# vector        point = [0, 0, 0]
# matrix

# Nested List
"""
1  2  3
4  5  6
7  8  9
"""

mat_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(len(mat_1))

print(mat_1[0][2])

print(mat_1[2][1])

mat_2 = [
    [
        [11, 12, 13],
        [21, 22, 23],
    ],
    [
        [101, 102, 103],
        [111, 112, 113],
    ],
]

print(mat_2[0][0][2])
print(mat_2[1][1][1])
print(mat_2[0][1][2])
print(mat_2[-1][1][-1])

mat_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    # [10, 11, 12]
]
mat_1.append([10, 11, 12])

print(mat_1)

mat_1[0].append(101)
mat_1[1].remove(6)
print(mat_1)

#
tup_1 = ((1, 2), (3, 4))
tup_1 = (
    (1, 2),
    (3, 4),
)

print(tup_1[1][0])

hello = (
    ('en', 'Hello'),
    ('np', 'नमस्ते'),
    ('jp', 'こんにちは'),
)

# Nested Dictionaary

# Structure:
"""
{
    'key': {
        'key': 'value',
        'key': 'value'
    }
}
"""

person = {
    'name': 'Ram',
    'age': 20,
    'father': {
        'name': 'Shyam',
        'age': 40,
        'father': {
            'name': 'Hari',
            'age': 60
        },
    },
}

print(person['name'])
print(person['father']['name'])
print(person['father']['father']['age'])
print(person['father']['father']['name'])

yoda = {
    'name': 'Yoda',
    'age': 900,
    'species': "Yoda's",
    'language': 'Galactic Basic',
    'affiliation': {
        'organization': 'Jedi',
        'member_size': 12,
        'weapons': ['Force', 'Lightsaber', 'swords', 'batons']
    },
    'weapon': 'lightsaber',
}

print(yoda['language'])
print(yoda['affiliation']['member_size'])
print(yoda['affiliation']['weapons'][-1])
print(yoda['affiliation']['weapons'][1])
print(yoda['weapon'])

print('language: ', yoda['language'].lower())
yoda['affiliation']['weapons'].append('Cannon')

yoda['affiliation']['member_size'] += 5

print(yoda)

students = [
    {
        'name': 'Kishor',
        'age': 20,
        'Major': 'Python'
    },
    {
        'name': 'Manish',
        'age': 22,
        'Major': 'Javascript'
    },
    {
        'name': 'Rajendra',
        'age': 24,
        'Major': 'Java'
    },
]
print(students[1])
print(students[0]['age'])
print(students[2]['age'] + 10)
students[0]['parent_name'] = ['Ram', 'Sita']
print(students[0])
students.append({'name': 'Reeti', 'age': 20, 'major': 'Oracle'})
del students[2]
print(students)
# students.pop(2)

x = {1, 2, 3, (4, 5, 6), 7, 8}

print(1 in x)

odd = [1, 3, 5, 7, 9]

print(1 in odd)
print(2 not in odd)

print(900 in yoda.values())

a = (
    (1, 2, 3),
    (4, 5, 6),
)

print(1 in a)  # False
print(1 in a[0])  # True
