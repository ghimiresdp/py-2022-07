x = [1, 2, 3, 4, 5]

# I want double of all numbers of list x into list y
# y = x * 2
# y = []
# for item in x:
#     y.append(2 * item)
#     print(item)

# print(y)

y = [2 * item for item in x]
y = [item**2 for item in x]
print(y)

m = 2
c = 5
x_values = [1, 2, 3, 4]

y_values = [m * x + c for x in x_values]

print(x_values, y_values)
print(x_values)
print(y_values)
print(list(zip(x_values, y_values)))
#

m = 2
c = 5
x_values = list(range(1, 9))

# y_values = [m * x + c for x in x_values if x%2 == 0]
results = [(x, m * x + c) for x in x_values if x % 2 == 0]
print(results)

m = 2
c1 = 5  # for all odd
c2 = 10  # for all even
x_values = list(range(1, 9))

results = [(x, m * x + (c2 if x % 2 == 0 else c1)) for x in x_values]
print(results)

x = [1, 2, 3, 4, 5]

y = {2 * item for item in x}

print(y)

# Create a comprehension that generates a dictionary of first 5 natural numbers and their cubes

cubes = {x: x**3 for x in range(1, 6)}

print(cubes)

#
hello = (
    ('en', 'Hello', 'Used to communicate with people'),
    ('np', 'नमस्ते', ''),
    ('fr', 'Bonjour',''),
    ('jp', 'こんにちは',''),
    ('ch', '你好',''),
)

# hello = dict(hello)

# print(hello)

dict_0 = {}
for key, value, _ in hello:
    dict_0[key] = value

print(dict_0)

dict_1 = {key: value for key, value, _ in hello}

print(dict_1)


x = [1, 2, 3, 4, 5]
y = (2 * item for item in x)

for item in y:
    print(item)

print(y)
