"""
# Bitwise Operators

- bitwise operators, as suggested by name, work on bit.
- bitwise operator works only with numeric values
- operation is done with each bit position rather than the value as a whole
- suppose we have 2 numbers `5` and `6`
We need to understand binary to decimal conversion and vice versa to understand bitwise operation

binary numbers are also known as base-2 numbers

** not just valid for python

- `5` in decimal is `101` in binary
- `16` in decimal is `10000` in binary

for uint8 or u8,

5   =   0 0 0 0    0 1 0 1
16  =   0 0 0 1    0 0 0 0

for uint32 or u32,

5   =   `0000 0000 0000 0000 0000 0000 0000 0101`

16  =   `0000 0000 0000 0000 0000 0000 0001 0000`

in the above example, we perform bitwise operation to same positioned digit
of the both numbers
    - the first digit of the first value interacts with the first digit of second value
    - the second digit of the first value interacts with the second digit of second value,
      ...
    - the last digit of the first value interacts with the the last digit of second value

you can always check the binary value of a number with
`bin()` function.


Some Bitwise Operations

- Bitwise AND operator `&`
- Bitwise OR operator `|`
- Bitwise NOT operator `~`
- Bitwise XOR operator `^`
- Bitwise SHIFT LEFT operator `<<`
- Bitwise SHIFT RIGHT operator `>>`


"""


"""
Bitwise AND
5   =    0 0 1 0 1
16  =    1 0 0 0 0
result = 0 0 0 0 0
"""

a =  5
b = 16

print(a and b)  # 16
print(a & b)    # 0

"""
Bitwise or
5   =    0 0 0 1 0 1
16  =    0 1 0 0 0 0
result = 0 1 0 1 0 1
"""
print(a or b)   # 5
print (a | b)   # 21

#
# 5   =        0 1 0 1
# ~5  =        1 0 1 0
# 1's Complement
# 2's Complement

print(~a)


"""
0 xor 0 = 0
0 xor 1 = 1
1 xor 0 = 1
1 xor 1 = 0

Bitwise xor
5   =      0 0 0 1 0 1
17  =      0 1 0 0 0 1
5 or 17 =  0 1 0 1 0 1
5 xor 17 = 0 1 0 1 0 0
"""
a = 5
b = 17

print(a | b)  # 21
print(a ^ b)  # 20


# 9 = 1 0 0 1

print('9 << 1 = ', 9 << 1)
print('9 << 2 = ', 9 << 2)
print('9 >> 1 = ', 9 >> 1)
print('9 >> 2 = ', 9 >> 2)
