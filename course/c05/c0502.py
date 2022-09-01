# Print the multiplication table from 4 to 7

num = 4

while num <= 7:
    mul = 1
    while mul <= 10:
        print(f'{num:>2}  X {mul:>2}  =  {(num * mul):>2}')
        mul += 1
    print()
    num += 1


# num = 4

# while num <= 7:
#     mul = 1
#     print(f'[ Table of {num} ]'.center(20, '-'))
#     while mul <= 10:
#         print(f'{num:>2} X {mul:>2} = {(num * mul):>2}'.center(20))
#         mul += 1
#     print()
#     num += 1
