"""
for (int x = 0; x < 10; x++){
    // code here
}
"""
"""
For Loops
"""

# Range

r1 = range(10)  # creates a range from 0 upto 9
r2 = range(1, 10)  # creates a sequence of numbers from 1 to 10
r3 = range(1, 10, 2)  # creates a sequence of numbers from 1 to 10 with step of 2
r4 = range(10, 1, -2)  # creates a sequence of numbers from 1 to 10 with step of -2

print(list(r4))

for x in range(10):
    if x > 8:
        break
    print('The value of x is: ', x)

word = 'Hello World!'
for x in word:
    print(f'The ASCII value of {x} is: {ord(x)}')

list1 = [1, 5, 8, 2, 10, 13]

index = 0

while index < len(list1):
    print(list1[index])
    index += 1

for item in list1:
    print(item)

# try to avoid this
# for index in range(len(list1)):
#     print(index, list1[index])

for index, item in enumerate(list1):
    print(index, item)

odd = {9, 1, 3, 7, 5}
double_odd = []
for num in odd:
    double_odd.append(2 * num)
print(double_odd)

person = {
    'name': 'Spock',
    'age': 90,
    'address': 'Vulcan',
}

for key, value in person.items():
    print(f'The {key} is {value}')

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for inner in nested:  # [1, 2, 3]
    # print(x)
    for item in inner:
        print(item, end=' ')
print()

nested = [2, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output [1, 2, 3, 4, 5, 6, 7, 8, 9]
out = []
for inner in nested:  # [1, 2, 3]
    if type(inner) is list:
        for item in inner:
            out.append(item)
    else:
        out.append(inner)
        # print(item, end=' ')

print(out)

lang = {
    'low level': ['Machine Level', 'Assembly'],
    'high level': ['C++', 'Java', 'Python'],
}

for key, value in lang.items():
    for lng in value:
        print(f'The {key} programming language is {lng}')
