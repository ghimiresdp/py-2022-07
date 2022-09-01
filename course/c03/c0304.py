# Dictionary
"""

Apple

Description of Apple



Ball

Description of Ball

- Dictionaries are similar to lists
- They are represented by key-value pairs
- dictionaries are ordered (since python 3.7)
- they are written inside curley brackets or braces {}
- keys must be unique otherwise the later one replaces the previous key-value pair
- dictionaries are mutable.
- dictionaries can have multiple data types in their key-value pair

"""
"""
Structure
{ key_1: value_1, key_2: value_2, ...}

{
    key_1: value_1,
    key_2: value_2,
    ...
}
"""
# %%
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': 'Lieutenant',
}

print(person)

print(type(person))

# %%

person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': 'Lieutenant',
    'age': 21,
}
print(person)

# %%
# person = ['Spock', 20, False, 'Lieutenant']

print(person['married'])

print(person['positions'])

# %%

detail = {
    'name': 'reeti',
    'salary': 40000,
    'job': ['analyst', 'developer'],
    'father': {
        'name': 'ABC',
    }
}
print(detail)

# %%

ram = {
    'sn': 1,
    'fn': 'Ram',
    'mn': 'Prasad',
    'occu': 'Farmer',
}

shyam = {
    'sn': 2,
    'fn': 'Shyam',
    'mn': 'Kumar',
    'occu': 'Officer',
}
# survey = [1, 2]
survey = [ram, shyam]

survey = [
    {
        'sn': 1,
        'fn': 'Ram',
        'mn': 'Prasad',
        'occu': 'Farmer',
    },
    {
        'sn': 2,
        'fn': 'Shyam',
        'mn': 'Kumar',
        'occu': 'Officer',
    },
]

print(survey)

# %%
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': ['Lieutenant', 'Captain', 'Commander'],
}

print(person['name'])
print(f"{person['name']} is {person['age']} years old.")

# %%
income = {'salary': 2000, 'lease': 1000, 'stock': 1200}

# %%
gross_income = income['salary'] + income['lease'] + income['stock']
# total_income = sum([income['salary'],income['lease'], income['stock']])
tax = gross_income * 0.20
net_income = gross_income - tax

print(net_income)

# %%

# Adding/Updating values of the dictionary

income = {
    'salary': 2000,
    'lease': 1000,
    'stock': 1200,
}

# 'freelancing': 500

# x = [1, 2, 3, 4, 5]
# x[-1] = 6
income['freelancing'] = 50  # adding new

income['lease'] = 1100  # updating the old one

print(income)

# adding / updating multiple values

other_values = {
    'uber': 600,
    # 'remittance': 700,
    'salary': 2400
}

income.update(other_values)

print(income)

#
x = {'name': 'dell', 'brand': 'dell'}

print(income['salary'])
# print(income['remittance'])       # KeyError
print(income.get('remittance'))  # Returns value if value exists else None
print(income.get('remittance', 100))  # Returns value if value exists else 0

person = {
    'name': 'John Doe',
    'age': 20
    # 'father_name': 'Sr.John Doe'
}

print(person.get('father_name', 'Unspecified'))

print(person.__len__())
print(len(person))

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

z = [*x, *y, 9, 10]



income = {
    'salary': 2000,
    'lease': 1000,
    'stock': 1200,
}

other_values = {
    'uber': 600,
    'remittance': 700,
    'salary': 2400
}

income = {
    **income,
    **other_values,
    'part_time_job': 1000,
    }

print(income)

"""
{
    'salary': 2400,
    'lease': 1000,
    'stock': 1200,
    'uber': 600,
    'remittance': 700,
    'part_time_job': 1000
}
"""
salary = income.pop('salary')
print(salary)
print(income)

stock=income.pop('stock')
print(stock)
print(income)


_, value = income.popitem()
print(value, sep='\n')
print(income)

#

del income['uber']
print(income)

#

print(income)

income_2 = income.copy()

income_2['lease'] = 1200

print(income)
print(income_2)


x = {
    'a': 5,
    'b': 6,
    'c': 12,
    'd': 100,
}

y = dict.fromkeys(['a', 'b'], 1)

print(y)

# print(y.get('c', 5))
y.setdefault('c', 5)
print(y['c'])
print(y)

y.clear()

print(y)


x = {
    'a': 5,
    'b': 6,
    'c': 12,
    'd': [100, 200, 300],
}

print(x.keys())     # dict_keys [key1, key2, ..]
# dict_keys(['a', 'b', 'c', 'd'])

print(x.values())   # dict_values [value1, value2, ...]
# dict_values([5, 6, 12, [100, 200, 300]])

print(x.items())    # dict_items [(key1, value1), (key2, value2), ...]
# dict_items([('a', 5), ('b', 6), ('c', 12), ('d', [100, 200, 300])])
